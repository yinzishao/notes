- 如何改变数组里面的元素,不能直接Mongoose doesn't create getters/setters for array indexes;
doc.array.set(3, 'changed');
doc.save();
注意：试验是doc.array才能有set方法。
如果是doc.{}.array.set()则报错

- 或者：
doc.array[3] = 'changed';
doc.markModified('array');
doc.save();

- findByIdAndUpdate/findByIdAndRemove
只能根据id查询并作update/remove操作，操作的数据仅一条
> 如果id在sheme中自己设置了mongoose.Schema.Types.ObjectId;mongoDB仍显示为_id，mongoose已改变。
- Schema#pre(method, callback)
Defines a pre hook for the document.
执行某个方法前，执行该callback。
eg:
toySchema.pre('validate', function (next) {
  if (this.name !== 'Woody') this.name = 'Woody';
  next();
})

- Query#\$method	对应mongo各种$方法

	chaining syntax

	Query#$where(js)

- population 
mongoDB并没有连接(join)操作，如果想引用其他集合的文档，可以使用population
   
	-  手动修改填充字段的时候不是像官方文档那样用一个文档对象去覆盖ref，而是对应的_id。


- validateSync();
    检测模型的字段是否符合要求

    自定义错误：
    var userSchema = new Schema({
      phone: {
        type: String,
        validate: {
          validator: function(v) {
            return /\d{3}-\d{3}-\d{4}/.test(v);
          },
          message: '{VALUE} is not a valid phone number!'
        },
        required: [true, 'User phone number required']
      }
    });

####更新（update）验证器

- Mongoose也支持update()和findoneandupdate()操作的验证。在Mongoose 4.x，更新验证器是默认关闭
开启更新验证器，设置runValidators选项为update() 或 findOneAndUpdate()。

- 更新（update）验证器和文档（document）验证器有一个主要的区别：**this**(获取该文档的其他值)
运行更新验证时，被更新的文件可能不在服务器的内存中，所以默认情况下这个值不定义。

- context 选项(更新不能用this.otherfiled)
context选项允许你在更新验证器设置此值为相关查询。
```this.getUpdate().$set.name.toLowerCase().indexOf('red') !== -1```

- 另一个主要差别，更新验证器只能运行在指定的路径中的更新。例如，在下面的示例中，因为在更新操作中没有指定“name”，更新验证将成功。
使用更新（update）验证器，required验证器验证失败时，你要明确地$unset这个key。

- 最后值得注意的一个细节：更新（update）验证器只能运行在 \$set 和 \$unset 选项。例如，下面的更新将成功，无论数字的值。

---

###注意：
> 使用global.promise的时候，返回的promise,eg:Content.find({route: r}).exec();传递了里面的错误信息。

---


> Model#save returns a promise, so you should skip the .exec():

---


###参考链接：
