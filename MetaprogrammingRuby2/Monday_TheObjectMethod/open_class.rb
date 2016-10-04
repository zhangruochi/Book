def to_alphanumeric(s)
    s.gsub(/[^\w\s]/,'')
end

to_alphanumeric '#3 *The //Magic )Number?'


#利用单元测试框架进行测试
require 'test/unit'
class ToAlphanumericTest < Test::Unit::TestCase
    def test_strip_non_alphanumeric_character
        assert_equal '3 The Magic Number', to_alphanumeric('#3 *The //Magic )Number?')
    end
end    

require 'test/unit/ui/console/testrunner'
Test::Unit::UI::Console::TestRunner.run(ToAlphanumericTest)  



#打开String类
class String
    def to_alphanumeric
        gsub(/[^\w\s]/,'')
    end
end


puts ''
print "1:",'#3 *The //Magic )Number?'.to_alphanumeric
puts ''

#细化  在模块的作用域内有效
module StringExtension
    refine String do
        def to_alphanumeric_2
            gsub(/[^\w\s]/,'')
        end
    end
end


module StringStuff
    using StringExtension
    print "2:",'#3 *The //Magic )Number?'.to_alphanumeric_2
end




puts ''
#'#3 *The //Magic )Number?'.to_alphanumeric_2  #没有找到该方法

#细化 从 using 语句开始到文件结束有效
using StringExtension
print "3:",'#3 *The //Magic )Number?'.to_alphanumeric_2





