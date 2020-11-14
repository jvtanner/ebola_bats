# ebola bats

After the Ebola outbreak of 2015, there was an urgent need to learn
more about the virus. You have been asked to uncover how a particular group of bat genes
impact an important trait: whether the bat can carry Ebola. Nobody knows the underlying
mechanism; it is up to you to hypothesize what is going on. For 100,000 independently sampled bats, you have collected data of whether or not five genes are expressed, and whether or not the bat can carry Ebola.  If a gene is expressed, it can affect both the probability of other genes being 1
expressed and the probability of the trait being expressed. You can find the data in a file called
bats.csv. A value of 1 denotes True, whereas a value of 0 denotes False. Each row in the file corresponds to one bat and has 6 columns that represent Boolean values:


● Boolean 0: Whether the 0th gene is expressed in the bat (G0)

● Boolean 1: Whether the 1st gene is expressed in the bat (G1)

● Boolean 2: Whether the 2nd gene is expressed in the bat (G2)

● Boolean 3: Whether the 3rd gene is expressed in the bat (G3)

● Boolean 4: Whether the 4th gene is expressed in the bat (G4)

● Boolean 5: Whether the trait is expressed in the bat; i.e., the bat can carry Ebola (T)

Follow the instructions in each subpart of this question to either write code or answer questions in your PDF. For code-writing questions, follow the following constraints so your code works
with our auto-grader:

● Do not modify the name or signature of any function we ask you to write, though you
may use helper functions if you wish. 

● You’ll write code in the file cs109_pset2.py, which you can download from the
course website. Submit only that file, and do not modify the name of that file. 

● Make sure your return values are in the format we expect as described below. 



A. [Coding] First, you will calculate the probability of the trait being expressed, namely
P (T), along with
P
(Gi) for each gene i.
 
In this part, you’ll write the function part_a. You should return a numpy array with shape (6, ). 
Mathematically, you can think of that as a row vector with 6 columns. The elements at indices 0 
through 4 should be 
P(G0), P (Gi), ... , P (G4)
 respectively, and the element at index 5 should be 
P
(T )
.


Here are some Python tips that you might find useful:

● We strongly recommend using numpy in this (and subsequent) questions.  You
can load a csv file into a numpy array named data by using 
np.genfromtxt: 

data = np.genfromtxt(filename, delimiter=',') 

● You can get the ith column from data using slicing by writing data[:, i]. 
That returns an array of shape (n, ) where n is the number of rows in the csv file.

● You can take the mean of a numpy array using the np.mean method. Example:

arr = np.array([1, 2, 3])       

print(arr.shape)     # Output: (3, ) 

print(np.mean(arr))          # Output: 2.0

● If you leverage the axis parameter in np.mean, your function will be just a few
lines long.


C. [Written] For each gene i, decide whether or not you think that is would be reasonable to
assume that Gi is independent of T. Support your argument with numbers. Remember that our 
probabilities are based on 100,000 bats, not infinite bats, and are therefore only estimates 
of the true probabilities. 

B. [Coding] For each gene i, calculate P
(T  | Gi )
.
In this part, you’ll write in the function part_b. You should return a numpy array with
shape (5, ). The element at index i should be P
(T  | Gi )
.
Just like in part (A), we’ve provided an autograder that runs on bats.csv, though we
might have additional hidden tests on a data file that’s different from the one we gave
you. If we do, we promise the file will be in the same format that’s described above.
Another Python tip to complement the ones listed above: check out the np.where
method. Specifically, if your csv is stored in a numpy array named data, you can store a
subset of the rows where the ith column is 1 with the following code:

subset = data[np.where(data[:, i] == 1)]

our probabilities are based on 100,000 bats, not infinite bats, and are therefore only estimates of the true probabilities. 
