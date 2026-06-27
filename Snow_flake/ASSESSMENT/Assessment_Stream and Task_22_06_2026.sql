-- Task and Stream                                      date : 23-06-2026

-- new table and copy table

CREATE OR REPLACE TABLE sales_source (
    id INT,
    product STRING,
    amount NUMBER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sales_source (id, product, amount) VALUES
(1, 'laptop', 1000),
(2, 'mobile', 500);

CREATE OR REPLACE TABLE sales_target LIKE sales_source;

select * from sales_source;

select * from sales_target;



-- stream on sales_source

CREATE OR REPLACE STREAM sales_stream ON TABLE sales_source;

select * from sales_stream;

-- Task on sales_target from sales_stream

CREATE OR REPLACE TASK load_new_sales
WAREHOUSE = compute_wh
SCHEDULE = '1 MINUTE'  -- runs every minute
AS
INSERT INTO sales_target(id, product, amount) 
SELECT id, product, amount
FROM sales_stream;

-- start or resume task

ALTER TASK load_new_sales suspend;

-- Task for Update, Delete and Insert


create or replace task load_new_sales_2
    warehouse = compute_wh
    schedule = '1 minute'
    when system$stream_has_data('sales_stream')

as
    merge into sales_target st
    using sales_stream ss
    on st.id = ss.id


-- 1. update

     when matched
        and ss.metadata$action = 'INSERT'
        and ss.metadata$isupdate = 'TRUE'
        then update set st.product = ss.product, st.amount = ss.amount

-- 2. delete

     when matched
        and ss.metadata$action = 'DELETE'
        and ss.metadata$isupdate = 'FALSE'
        then delete
        
-- 3. insert

   when not matched
       and ss.metadata$action = 'INSERT'
       and ss.metadata$isupdate = 'FALSE'
       then insert (id,product,amount) values (ss.id, ss.product, ss.amount);

alter task load_new_sales_2 resume;

insert into sales_source (id,product,amount) values(5,'gpu',50000);

update sales_source set product = 'ram', amount = 9000 where id = 4; 

delete from sales_source where id = 5; 