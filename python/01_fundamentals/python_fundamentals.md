# 00. CREATING PYTHON MODULES (*.py)
## 00.00 Naming conventions
### Camel case 🐪
- First letter lowercase
- First letter of each new word uppercase
- `thingsToDo` `finalValue`
### Pascal case 🦎
- Also known as "upper camel case" or "capital case"
- The first letter of each word is uppercase
- `FriendsName` `FinalValue`
### Snake case 🐍
- Also known as "underscore case"
- Underline in place of space to separe words
- When is all in upper case, is called "screaming snake case"
- `friends_name` `final_value`
### Kebab case 🌯
- Use dash to combine words
- In upper case is "screaming kebab case"
- `things-to-do` `final-value`

## 00.01 Naming conventions in different programming languages.

### Java Naming Conventions ☕

- camelCase for variables, attributes, and methods;
- PascalCase for classes, enums, and interfaces;
- SCREAMING_SNAKE_CASE for constants.

```java
public class Person {
    public static void main(String[] args) {
        String firstName = "Maria";
        int age = 22;
        double currentHeight = 1.65;
        final String DEFAULT_MESSAGE = "Hello";
    }
}
```

### JavaScript Naming Conventions 🇯 🇸

- camelCase for variables, constants, functions, and methods;
- PascalCase for classes.

```javascript
class BankClient {  
    constructor(firstName, cpf) { 
        this.firstName = firstName;
        this.cpf = cpf;
    }

    displayFirstName(){
        console.log(this.firstName);
    }
}

var clientOne = new BankClient('Maria', 150);
var clientTwo = new BankClient('João', 70);
```

### Python Naming Conventions 🐍

- snake_case for variables, functions, and methods;
- PascalCase for classes;
- SCREAMING_SNAKE_CASE for constants.

```python
class Person:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

    def display_first_name(self):
        print(self.name)

person_one = Person('Alice', '123456789')
```

### Go Naming Conventions 🔷

- PascalCase for exported names (accessible outside the package);
- camelCase for internal names (not exported).

```go
package name

type ExportedStruct struct {
    unexportedField string
}
```

### Ruby Naming Conventions 🔻

- PascalCase for classes and modules;
- snake_case for methods, variables, file and directory names;
- SCREAMING_SNAKE_CASE for constants.

```ruby
class Person
    def initialize(first_name, cpf)
        @first_name = first_name
        @cpf = cpf
    end

    def display_first_name
        @first_name
    end
end

person_one = Person.new('Alice', 123456789)
```

# 01. COMMENTS
- We use the `#` to tell the interpreter to ignore evertything after;
- `#` are used to important notes and informations.
```python
# print hello world
print("hello world")
```
## Docstring
- Is a multi-line comment;
- The interpreter reads this, different from the comments, but does nothing 
- `"""` or `'''`
```python
"""
I can use
as a multi-line
comment
"""
```

# 02. PRINT FUNCTION
