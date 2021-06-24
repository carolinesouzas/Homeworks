#!/usr/bin/env python
# coding: utf-8

# # Homework 5, Part 1: Building a pandas cheat sheet
# 
# **Use `animals.csv` to answer the following questions.** The data is small and the questions are pretty simple, so hopefully you can use this for pandas reference in the future.

# ## 0) Setup
# 
# Import pandas **with the correct name**.

# In[1]:


import pandas as pd


# ## 1) Reading in a csv file
# 
# Use pandas to read in the animals CSV file, saving it as a variable with the normal name for a dataframe

# In[2]:


df = pd.read_csv("animals.csv")


# ## 2) Checking your data
# 
# Display the number of rows and columns in your data. Also display the names and data types of each column.

# In[10]:


df.count()


# In[9]:


df.columns


# In[8]:


df.dtypes


# ## 3) Display the first 3 animals
# 
# Hmmm, we know how to take the first 5, but maybe the first 3. Maybe there is an option to change how many you get? Use `?` to check the documentation on the command.

# In[12]:


df.head(3)


# ## 4) Sort the animals to show me the 3 longest animals
# 
# > **TIP:** You can use `.head()` after you sort things!

# In[14]:


df.sort_values(by='length', ascending=False).head(3)


# ## 5) Get the mean and standard deviation of animal lengths
# 
# You can do this with separate commands or with a single command.

# In[19]:


df.length.mean(), df.length.std()


# ## 6) How many cats do we have and how many dogs?
# 
# You only need one command to do this

# In[23]:


df.groupby(by= 'animal').count()


# ## 7) Only display the dogs
# 
# > **TIP:** It's probably easiest to make it display the list of `True`/`False` first, then wrap the `df[]` around it.

# In[25]:


df[df.animal == 'dog']


# In[ ]:





# In[ ]:





# In[ ]:





# ## 8) Only display the animals that are longer than 40cm

# In[26]:


df[df.length > 40]


# ## 9) `length` is the animal's length in centimeters. Create a new column called `inches` that is the length in inches.

# In[29]:


df['inches'] = df.length * 0.393701
df.head()


# ## 10) Save the cats to a separate variable called `cats`. Save the dogs to a separate variable called `dogs`.
# 
# This is the same as listing them, but you just save the result to a variable instead of looking at it. Be sure to use `.head()` to make sure your data looks right.
# 
# Once you do this, every time you use `cats` you'll only be talking about the cats, and same for the dogs.

# In[30]:


cats = df[df.animal == 'cat']


# In[31]:


dogs = df[df.animal == 'dog']


# In[32]:


dogs.head() , cats.head()


# ## 11) Display all of the animals that are cats and above 12 inches long.
# 
# First do it using the `cats` variable, then also do it using your `df` dataframe.
# 
# > **TIP:** For multiple conditions, you use `df[(one condition) & (another condition)]`

# In[33]:


cats[cats.inches > 12].head()


# In[34]:


df[(df.animal == 'cat') & (df.inches > 12)].head()


# In[ ]:





# ## 12) What's the mean length of a cat? What's the mean length of a dog?

# In[35]:


cats.length.mean()


# In[36]:


dogs.length.mean()


# In[ ]:





# ## 13) If you didn't already, use `groupby` to do #12 all at once

# In[37]:


df.groupby(by= 'animal').length.mean()


# ## 14) Make a histogram of the length of dogs.
# 
# We didn't talk about how to make a histogram in class! It **does not** use `plot()`. Imagine you're a programmer who doesn't want to type out `histogram` - what do you think you'd type instead?
# 
# > **TIP:** The method is four letters long
# >
# > **TIP:** First you'll say "I want the length column," then you'll say "make a histogram"
# >
# > **TIP:** This is the worst histogram ever

# In[45]:



dogs['length'].hist()


# ## 15) Make a horizontal bar graph of the length of the animals, with the animal's name as the label
# 
# > **TIP:** It isn't `df['length'].plot()`, because it needs *both* columns. Think about how we did the scatterplot in class.
# >
# > **TIP:** Which is the `x` axis and which is the `y` axis? You'll notice pandas is kind of weird and wrong.
# >
# > **TIP:** Make sure you specify the `kind` of graph or else it will be a weird line thing
# >
# > **TIP:** If you want, you can set a custom size for your plot by sending it something like `figsize=(15,2)`

# In[53]:


df.plot(kind='barh', xlabel='name', ylabel='length', x='name',y='length')


# ## 16) Make a sorted horizontal bar graph of the cats, with the larger cats on top
# 
# > **TIP:** Think in steps, even though it's all on one line - first make sure you can sort it, then try to graph it.

# In[57]:


cats.sort_values(by='length', ascending=True).plot(kind='barh', xlabel='name', ylabel='length', x='name',y='length')


# ## 17) As a reward for getting down here: run the following code, then plot the number of dogs vs. the number of cats
# 
# > **TIP:** Counting the number of dogs and number of cats does NOT use `.groupby`! That's only for calculations.
# >
# > **TIP:** You can set a title with `title="Number of animals"`

# In[58]:


import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# In[83]:


df.groupby(by= 'animal').agg(['count', 'sum'])


# In[85]:


df.animal.value_counts().plot(kind = 'bar')

