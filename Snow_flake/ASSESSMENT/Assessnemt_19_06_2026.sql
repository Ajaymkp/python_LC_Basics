--  Shredding json data                                       Date : 18-06-2026 to 19-06-2026

-- =====================================================
-- ASSIGNMENT 1 : CUSTOMER ORDERS 
-- =====================================================
-- TASKS:
-- 1. Create the table and load the sample data.
-- 2. Extract customer_name and city from ORDER_INFO.
-- 3. Display all products purchased by each customer.
-- 4. Display product name and price separately.
-- 5. Count how many products each customer purchased.
-- 6. Find the total order value for each customer.
-- 7. Write the solution using JSON path notation and array handling.

CREATE OR REPLACE TABLE CUSTOMER_ORDERS (
    ORDER_ID INT,
    ORDER_INFO VARIANT
);

INSERT INTO CUSTOMER_ORDERS
SELECT
    101,
    PARSE_JSON('{
        "customer_name":"John Doe",
        "city":"Chennai",
        "orders":[
            {"product":"Laptop","price":55000},
            {"product":"Mouse","price":1200},
            {"product":"Keyboard","price":2500}
        ]
    }');

INSERT INTO CUSTOMER_ORDERS
SELECT
    102,
    PARSE_JSON('{
        "customer_name":"Priya",
        "city":"Bangalore",
        "orders":[
            {"product":"Mobile","price":30000},
            {"product":"Earbuds","price":2500}
        ]
    }');

-- Tasks
-- 2. Extract customer_name and city from ORDER_INFO.
select * from customer_orders;
select order_id,
order_info:customer_name::string as customer_name,
order_info:city::string as city
from customer_orders;

-- 3. Display all products purchased by each customer.

select order_id,
order_info:customer_name::string as customer_name,
-- order_info:orders::variant as orders,
f.value:product as products
from customer_orders,
LATERAL FLATTEN(input => ORDER_INFO:orders) f;

-- 4. Display product name and price separately.

SELECT order_id,
f.value:product as products,
f.value:price as prices
from customer_orders,
LATERAL FLATTEN(input => ORDER_INFO:orders) f;

-- 5. Count how many products each customer purchased.

select order_id,
order_info:customer_name::string as customer_name,
count(f.value:product) as count_products
from customer_orders ,
LATERAL FLATTEN(input => ORDER_INFO:orders) f
group by order_id,customer_name;

-- 6. Find the total order value for each customer.

select order_id,
order_info:customer_name::string as customer_name,
sum(f.value:price) as order_value
from customer_orders ,
LATERAL FLATTEN(input => ORDER_INFO:orders) f
group by order_id,customer_name;

-- 7. Write the solution using JSON path notation and array handling.
select * from customer_orders;
select order_id,
order_info['city'] as city,
order_info['customer_name'] as customer_name,
order_info['orders'][0]['price'] as first_price,
order_info['orders'][0]['product'] as first_product,
ARRAY_SIZE(order_info['orders']) as count_orders

-- 0 not_working
-- order_info['orders'][-1]['price'] as first_price,
-- order_info['orders'][-1]['product'] as first_product
from customer_orders;

-- =====================================================
-- ASSIGNMENT 2 : STUDENT COURSES
-- =====================================================
-- TASKS:
-- 1. Create the table and load the sample data.
-- 2. Extract student_name and department.
-- 3. Display all courses taken by each student.
-- 4. Display one row per course.
-- 5. Count the number of courses enrolled by each student.
-- 6. Identify students enrolled in a specific course.
-- 7. Use array processing techniques on the courses array.

CREATE OR REPLACE TABLE STUDENT_DATA (
    STUDENT_ID INT,
    STUDENT_INFO VARIANT
);

INSERT INTO STUDENT_DATA
SELECT
    1,
    PARSE_JSON('{
        "student_name":"Arun",
        "department":"Computer Science",
        "courses":["SQL","Python","Snowflake","Power BI"]
    }');

INSERT INTO STUDENT_DATA
SELECT
    2,
    PARSE_JSON('{
        "student_name":"Meena",
        "department":"Information Technology",
        "courses":["Java","AWS","Tableau"]
    }');

-- TASKS

-- 2. Extract student_name and department.

select student_id,
student_info:student_name::string as student_name,
student_info:department::string as departent
from student_data;


-- 3. Display all courses taken by each student.

select student_id,
student_info:student_name::string as student_name,
student_info:department::string as departent,
student_info:courses as courses,
from student_data;

-- 4. Display one row per course.

select c.student_id,
c.student_info:student_name::string as student_name,
c.student_info:department::string as departent,
f.value::string as corses,
from student_data c,
lateral flatten (input => student_info:courses)f;

-- 5. Count the number of courses enrolled by each student.

select student_id,
student_info:student_name::string as student_name,
count(f.value::string) as count_courses,
from student_data,
lateral flatten (input => student_info:courses)f
group by student_id,student_name order by student_id asc;

-- 6. Identify students enrolled in a specific course.

select c.student_id,
c.student_info:student_name::string as student_name,
f.value::string as corses,
from student_data c,
lateral flatten (input => student_info:courses)f
WHERE f.value::string = 'Snowflake';

-- 7. Use array processing techniques on the courses array.

SELECT 
    student_id,
    student_info:student_name::string AS student_name,
    ARRAY_SIZE(student_info:courses) AS total_courses,              -- Finds array length
    student_info:courses[0]::string AS first_course,                 -- Retrieves item at index 0
    ARRAY_CONTAINS('Python'::variant, student_info:courses) AS takes_python -- Returns TRUE/FALSE
FROM student_data;

-- =====================================================
-- ASSIGNMENT 3 : COMPANY PROJECTS
-- =====================================================
-- TASKS:
-- 1. Create the table and load the sample data.
-- 2. Extract project_name and manager.
-- 3. Display all team members for each project.
-- 4. Display one row per team member.
-- 5. Count the number of team members in each project.
-- 6. Find projects handled by a specific manager.
-- 7. Practice working with arrays stored in VARIANT columns.

CREATE OR REPLACE TABLE PROJECT_DATA (
    PROJECT_ID INT,
    PROJECT_INFO VARIANT
);

INSERT INTO PROJECT_DATA
SELECT
    1001,
    PARSE_JSON('{
        "project_name":"Data Warehouse Migration",
        "manager":"Ravi",
        "team_members":[
            "Kumar",
            "Suresh",
            "Anitha",
            "Divya"
        ]
    }');

INSERT INTO PROJECT_DATA
SELECT
    1002,
    PARSE_JSON('{
        "project_name":"Customer Analytics",
        "manager":"Priya",
        "team_members":[
            "Raj",
            "Deepa",
            "Vijay"
        ]
    }');

SELECT * FROM PROJECT_DATA;

-- 2. Extract project_name and manager.

select project_id,
project_info:project_name::string as project_name,
project_info:manager::string as project_manaager
from project_data;

-- 3. Display all team members for each project.


select project_id,
project_info:project_name::string as project_name,
project_info:team_members as team_members,
from project_data;

-- 4. Display one row per team member.

select project_id,
project_info:project_name::string as project_name,
f.value::string as team_members,
from project_data,
lateral flatten (input => project_info:team_members)f;

-- 5. Count the number of team members in each project.

select project_id,
project_info:project_name::string as project_name,
count(f.value::string) as count_team_members,
from project_data,
lateral flatten (input => project_info:team_members)f
group by project_id,project_name;

-- 6. Find projects handled by a specific manager.

select project_id,
project_info:project_name::string as project_name,
project_info:manager::string as manager
from project_data
where project_info:manager::string = 'Ravi';

-- 7. Practice working with arrays stored in VARIANT columns.

select project_id,
project_info['manager'] as manager,
project_info['project_name'] as project_name,
project_info['team_members'] as team_members,
project_info['team_members'][0] as first_team_members,
ARRAY_SIZE(project_info['team_members']) as count_team_members,
ARRAY_CONTAINS('Vijay'::variant, project_info:team_members) as is_or_not_members
from project_data;

-- ------------------------------------------------------------------------------------------------------------------------------------------------------------