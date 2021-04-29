# SQLPlus使用技巧

1. 查看缓存命令

    ```sql
    list
    ```

2. 清屏

    ```sql
    ho cls
    --------------------------------------
    clear screen
    ```

3. 设置每行显示的数据长度

    ```sql
    set linesize 500
    ```

4. 设置每次显示的数据行数

    ```sql
    set pagesize 50
    ```

5. 设置列宽
a表示字符型，大小写均可
9表示数字型，一个9表示一个数字位

    ```sql
    column ename format a20;
    column empno format 9999;
    ```

6. 使用/杠，执行最近一次的SQL语句

    ```sql
    /
    ```

7. spool命令，保存SQL语句和执行的结果

    ```sql
    spool "E:\GitHub repositories\Uplearning\Read\Oracle\knowledge\Material\spool_1"
    select * from emp;--示例SQL
    spool off
    ```

    - 可使用SPOOL保存查询的结果集
    - 可使用SPOOL命令生成一些动态的批量处理的脚本

8. 使用@命令，将文件读到orcl实例中并执行

    ```sql
    @ "E:\GitHub repositories\Uplearning\Read\Oracle\knowledge\Material\xplan.sql"
    ```

9. 把缓冲区中最后一条SQL语句调入记事本中进行编辑

    ```sql
    edit
    ```

10. 显示表结构

    ```sql
    desc--desc+空格+表名
    ```

11. 设置显示处理结果行数

    ```sql
    set feedback on;
    ```

12. 输出域标题

    ```sql
    set heading on;
    ```

13. 允许输出dbms_output

    ```sql
    set serveroutput on;
    ```

14. 显示执行时间

    ```sql
    set timing on; 
    ```

15. 输出域分隔符(列之间的分割符)

    ```sql
    set colsep' ';
    ```
