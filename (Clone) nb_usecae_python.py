# Databricks notebook source
# MAGIC %md
# MAGIC 1. ## Terinary operator : Implement using terinary operator whether water is boiling in given temperature or not?
# MAGIC
# MAGIC       syntax - value_true if else value_false
# MAGIC
# MAGIC

# COMMAND ----------

tem = 190

"This is a boiling water" if tem >90 else "Water is in normal temperature"

# COMMAND ----------

# MAGIC %md
# MAGIC ##2. Contol folow:Read using a wiget prommeining language you want to learn. Using contro flow, write a program to specifi which course uses the given programming laungauge.

# COMMAND ----------

dbutils.widgets.text("input","Python","Enter you desire Programming language")

progrmamming_laungauge = dbutils.widgets.get("input")

if progrmamming_laungauge =="python":
    print("Its required for all daat uses")
else:
    print("This used for all full stack development")

# COMMAND ----------

dbutils.widgets.text("input","Python","Enter you desire Programming language")

progrmamming_laungauge = dbutils.widgets.get("Programminglaungauge1")

if progrmamming_laungauge =="python":
    print("Its required for all daat uses")
else:
    print("This used for all full stack development")

# COMMAND ----------

dbutils.widgets.text("input","Python","Enter you desire Programming language")

progrmamming_laungauge = dbutils.widgets.get("Programminglaungauge1")

if progrmamming_laungauge =="python":
    print("Its required for all daat uses")
elif progrmamming_laungauge=="R":
    print("It's a part of Data science")
elif progrmamming_laungauge=="C":
    print("It is uiversal language")
else:
    print("This used for all full stack development")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Dog Breed Recommendations
# MAGIC Suppose we are helping people to pick a dog breed where users provide the following information:
# MAGIC
# MAGIC dog_person: Boolean representing if they are a dog person or not
# MAGIC cat_person: Boolean representing if they are a cat person or not
# MAGIC age: The user's age
# MAGIC Based on the user's input to these questions, we print out a recommendation.
# MAGIC
# MAGIC Our application works like this:
# MAGIC
# MAGIC If the user is not an adult (under the age of 18), we tell them to ask their parents for permission.
# MAGIC
# MAGIC Otherwise,
# MAGIC
# MAGIC If they are both a dog person and a cat person, we recommend Golden Retriever, since they get along well with cats.
# MAGIC If they are a dog person, but not a cat person, we recommend Scottish Deerhound, since they are known to chase cats.
# MAGIC If they are a cat person, but not a dog person, we tell them they're barking up the wrong tree.
# MAGIC Finally, if they are neither a dog person or a cat person, we ask them to evaluate whether a pet is right for them.

# COMMAND ----------

dog_lover = False
cat_lover = True

age = 16

if age <18:
    print ("Ask you parent for permission")
else:
    if dog_lover ==True and cat_lover == True:
        print("Goldern Retriver")
    elif dog_lover ==True and cat_lover == False:
        print ("Scottish Deerhound")
    elif dog_lover== False and cat_lover== True:
        print("They're barking up the wrong tree")
    else:
        print("Evaluate whether a pet is right for You.")
    



# COMMAND ----------

# MAGIC %md
# MAGIC ##Write a programme with a function that can return square of given value
# MAGIC

# COMMAND ----------

def square_number(number):
    print (number*number)

square_number(3)

#Another way of doing

def square_number(number:int):
    return(number*number)

square = square_number(36.5)
print(square)


# COMMAND ----------

# MAGIC %md
# MAGIC ## Write a Python code, sum of all the given number using for loop and Tupe
# MAGIC

# COMMAND ----------

nums = (1,2,3,4,5)

sum_numm = 0

for num in nums:
    sum_numm = sum_numm + num

print(f'sum of number is {sum_numm}')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Given a number, finds it's factirial using while loop
# MAGIC  

# COMMAND ----------

num = 6

factorial = 1

while num > 0:
     factorial = factorial * num

     num = num - 1

print (factorial)

# COMMAND ----------

assert 1==1
assert 1==2

# COMMAND ----------

Weatherinformation = dbutils.widgets.get("Weather Type")

assert Weatherinformation != "storm","stop landing of all flight"
assert Weatherinformation != "heavy rain","stop landing of all flight"

# COMMAND ----------

# MAGIC %run ./Shared/Introduction to Python forData Science andData Engineering - v1.1.6/Includes/run_example
# MAGIC greet(bob)

# COMMAND ----------



# COMMAND ----------

#Create the class (blueprint)

class Dog():
 pass

# COMMAND ----------

# Create object of a class 

my_dog = Dog()

type (my_dog)

# COMMAND ----------

class updated_dog:

    def methord_name(self,name):
        return f"name: {name}"

# COMMAND ----------

my_updated_dog = updated_dog()

my_updated_dog.methord_name("Tommy")

# COMMAND ----------


