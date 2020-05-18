backend

跳坑指南：

1.如果修改了模型model后migrate不可以的话，报错:no such column或者datatype dismatch， 可以试试删除db.sqlite3.原因不明，可能是django后端的问题，不能很好的支持主键修改等操作