# Ad-hoc polymorphism
# Created or done for a particular purpose as necessary.
# Ad-hoc polymorphism usually refers to code that appears to be polymorphic to the programmer, but
# the actual implementation is not. A typical example is overloading: using the same function name for
# functions with different kinds of parameters. Although it looks like a polymorphic function to the
# code that uses it, there are actually multiple function implementations (none being polymorphic) and
# the compiler invokes the appropriate one. Ad-hoc polymorphism is a dispatch mechanism: the type
# of the arguments is used to determine (either at compile time or run time) which code to invoke

# Parametric polymorphism
# Parametric polymorphism refers to code that is written without knowledge of the actual type of the
# arguments; the code is parametric in the type of the parameters. Examples include polymorphic
# functions in ML, or generics in Java 5.
# Type generics

# Subtype polymorphism
# Gives a single term many types using the subsumption rule. For example, a
# function with argument τ can operate on any value with a type that is a subtype of τ .