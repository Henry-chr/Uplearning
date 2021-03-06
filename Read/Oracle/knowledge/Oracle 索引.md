# Oracle 索引

## 简介

&emsp;&emsp;索引是建立在表上的可选数据库对象，是一组排序后的的索引键。主要用于加快数据的检索，类似于书籍的目录，快速定位到目标数据。索引在物理上和逻辑上都是独立的，创建或删除索引对基表不会有影响。当对基表进行DML操作时Oracle会自动管理索引，无需手动处理。

## 索引分类

### 结构分类

- 分区索引

        索引按范围（Range）或散列（Hash，Oracle 10g中引入）进行分区
        一个分区索引可能指向任何（或全部的）表分区。

- B-Tree索引

        B-Tree索引是一个典型的树结构，通常包含根节点、分支节点、叶子节点
        包括正常索引或反转关键字索引

- 位图索引

        位图索引主要针对大量相同值的列而创建
        位图索引不直接存储ROWID，而是存储字节位到ROWID的映射
        位图索引的空间占用明显小于B-Tree索引
        位图索引不适合经常更新的表
        关键字BitMap

### 逻辑分类

- 单列索引

        索引列为单个字段

- 组合索引

        索引列为多个字段，最多为32列，顺序自定义

- 唯一索引

        索引列的值唯一，Oracle会自动在表的主键列上创建唯一索引，关键字UNIQUE INDEX

- 非唯一索引

        索引列的值允许重复

- 函数索引

        一列或多列上的基于函数表达式所创建的索引
        表达式不能出现聚合函数
        不能在LOB类型的列上创建
        创建时必须具有 QUERY REWRITE 权限

- 反向键索引

        反向键索引反转索引列键值的每个字节，实现索引的均匀分配
        通常建立在值是连续增长的列上，使数据均匀地分布在整个索引上
        关键字REVERSE

## 创建索引原则

1. 权衡索引个数与DML之间关系

        建立索引的目的是为了提高查询效率的
        但建立的索引过多，会影响插入、删除数据的速度

2. 尽量将表和索引放在不同的表空间

        在读取数据时表与索引是同时进行的。
        表与索引在一个表空间里就会产生资源竞争，放在不同的表空间最佳。

3. 创建索引会产生Redo信息和占用磁盘空间

        索引是数据库对象之一，需要分配磁盘空间去存储。
        创建索引会产生Redo信息，对于大表创建索引时可以设置不产生日志信息。

4. 创建索引需根据具体的业务SQL

        Oracle根据具体的情况判断是否走索引。
        索引建在Where限制条件、表连接、需排序字段上。

5. 唯一索引优先

        如果同时存在唯一性索引和非唯一索引，oracle将使用唯一性索引而忽略非唯一索引

6. 经常用的字段放组合索引第一列

        组合索引只有它的第一列被where子句引用时，优化器才会使用该索引

7. 限制表中索引的数量

        索引会占用物理空间，会随基表数据量的增大而增大；
        当对表中的数据进行DML时，索引也要动态的维护，降低了数据的维护速度

8. 小表不要建索引

9. 对于基数大的列适合建立B树索引，对于基数小的列适合建立位图索引

10. 列中有很多空值，但经常查询该列上非空记录时应该建立索引

11. LONG（可变长字符串数据，最长2G）和LONG RAW（可变长二进制数据，最长2G）列不能创建索引

## 索引可选项

- NOSORT

    建立索引时会先对表记录排序再建立索引，当表数据量较多是会占用较多的时间。
    特殊情况下，我们就可以使用该参数加快建索引的速度。

```sql
CREATE INDEX IDX_TEMP_CHR_D_NOSORT ON TEMP_CHR_D (LIST_ID) NOSORT;
```

- ONLINE

    数据库系统默认是不允许DML与创建索引同时进行的，ONLINE选项可以避免此类问题，但会延长建索引时间。

```sql
CREATE INDEX IDX_TEMP_CHR_D_NOSORT ON TEMP_CHR_D (LIST_ID) ONLINE;
```

- NOLOGGING

    是否需要记录日志信息，一般用在在大型表上建索引，使用该参数，默认是记日志。

```sql
CREATE INDEX IDX_TEMP_CHR_D_NOSORT ON TEMP_CHR_D (LIST_ID) NOLOGGING;
```

- COMPUTE STATISTICS

    该参数会提示数据库建索引的同时，更新对应的统计信息。
    当数据修改量比较大的情况下，使用该选项有可能导致执行计划的不稳定。

```sql
CREATE INDEX IDX_TEMP_CHR_D_NOSORT ON TEMP_CHR_D (LIST_ID) COMPUTE STATISTICS;
```

- PARALLEL

    增加并发，多服务进程创建索引,通常针对大表建索引使用

```sql
CREATE /*+ PARALLEL(2)*/ INDEX IDX_EMP_ENAME ON EMP (ENAME);
```

## 索引失效分析

1. Where条件有不等于操作符(<>, !=)

2. 限定条件中有对空值的判断（Null或Not Null）

3. 非函数索引，Where条件中对索引列使用了函数

4. 不匹配的索引数据类型

5. 全模糊查询（'like '%aa'）

6. Union替换Or

7. 用EXISTS替代IN、用NOT EXISTS替代NOT IN

## 索引相关视图

|视图|说明|
|-|-|
|dba_indexes all_indexes user_indexes|这类视图显示索引的基本信息，如索引名称、索引是否压缩存储、索引段的存储等信息以及使用dbms_stats包或analyze语句生成的统计信息|
|dba_ind_columns all_ind_columns user_ind_columns|这类视图显示了被索引列的信息|
|dba_ind_expressions all_ind_expresions user_ind_expressions|这类视图显示函数索引的函数语句|
|dba_ind_statistics all_ind_statistics user_ind_statistics|这类视图显示对索引的优化统计信息|
|index_stats index_histogram|显示最近一次使用analyze index... validate structure语句生成的统计信息|
|v$object_usage|存储由alter index ... monitoring usage语句生成的索引使用信息|
