For full view pdf go here [[main-hashtable.pdf]]

**NOTES BELOW PDF**

![[main-hashtable.pdf]]

**Two types:** 
1. Non Separate Chaining
2. Separate Chaining

___

##### Non Separate Chaining

**Input Table**

| Name  | Height |
| ----- | ------ |
| Abe   | 6.5    |
| Tom   | 5.5    |
| Annie | 5.9    |

```C++
class NameHeight
{
	public:
		std::string name;
		double height;
};

NameHeight h[10];
std::pair <std::string, double> h[10];

```

```C++
// Send this into class above
std::pair <std::string, double>;
abe = {"Abe", 6.5};
```

###### **Hash Function**
There exists an 
```c++
std::hash
```

Pseudo Code

```
h("Abe")
= int('A') + int('b') * 10 + int('e') x 10^2
= 11145

"Abe"'s index is 11145 % 10  // 10 <- size of table
= 5

h("Tom") = 12094
12094 % 10 = 4

Find "Abe"'s hieght:
--------------------------
h("Abe") = 11145 % 10 = 5
--------------------------
This operation inbetween the ines is O(1)
```

**Output Table after these operations**

|     | Name | Height |
| --- | ---- | ------ |
| 0   |      |        |
| 1   |      |        |
| 2   |      |        |
| 3   |      |        |
| 4   |      |        |
| 5   | Abe  | 6.5    |
| 6   | Tom  | 5.5    |
| 7   |      |        |
| 8   |      |        |
| 9   |      |        |
With the above Hash Function an error could occur when you try to input Annie because there could be a hash collision due to moding 10

```
h("Annie") % 10 = (int('A') + 0 + ....) % 10
= 5
```


![[Hashtables 2024-11-14 12.54.10.excalidraw]]


To handle possible garbage remember to have some sort of flag to say when a "spot" is occupied. 

**New Table Including Flag**

|     | Name  | Height | State    |
| --- | ----- | ------ | -------- |
| 0   |       |        | AVAL     |
| 1   |       |        | AVAL     |
| 2   |       |        | AVAL     |
| 3   |       |        | AVAL     |
| 4   |       |        | AVAL     |
| 5   | Abe   | 6.5    | NOT AVAL |
| 6   | Tom   | 5.5    | NOT AVAL |
| 7   | Annie | 5.9    | NOT AVAL |
| 8   |       |        | AVAL     |
| 9   |       |        | AVAL     |
Delete Abe

|     | Name    | Height  | State        |
| --- | ------- | ------- | ------------ |
| 0   |         |         | AVAL         |
| 1   |         |         | AVAL         |
| 2   |         |         | AVAL         |
| 3   |         |         | AVAL         |
| 4   |         |         | AVAL         |
| 5   | ~~Abe~~ | ~~6.5~~ | ~~NOT AVAL~~ |
| 6   | Tom     | 5.5     | NOT AVAL     |
| 7   | Annie   | 5.9     | NOT AVAL     |
| 8   |         |         | AVAL         |
| 9   |         |         | AVAL         |

|     | Name  | Height | State    |
| --- | ----- | ------ | -------- |
| 0   |       |        | AVAL     |
| 1   |       |        | AVAL     |
| 2   |       |        | AVAL     |
| 3   |       |        | AVAL     |
| 4   |       |        | AVAL     |
| 5   |       |        | AVAL     |
| 6   | Tom   | 5.5    | NOT AVAL |
| 7   | Annie | 5.9    | NOT AVAL |
| 8   |       |        | AVAL     |
| 9   |       |        | AVAL     |

--- 

A good has function has to be two things.
1. Fast
2. Random

Design of hash functions is difficult. There are a few general a requirement that if given a key. Example below. 

1. The following must hold. The 2 strings of bits even if they are very similar, then the two hash values must be very very different.

| Key1 | 0   | (k1) very diff from (k2) |
| ---- | --- | ------------------------ |
| Key2 | 1   | (k2) very diff from (k1) |

2. Must use ***<u>All</u>*** the info in key
3. If there is only partial information for the first part of the key. It is impossible to know the second part of the key. It is possible to use it in such a way where if only using part of a key you could still create a collision. This should <u>NOT</u> happen.



##### Separate Chaining

Create an array of *generally* singly-linked-lists


| 0   | [x] |
| --- | --- |
| 1   | [x] |
| 2   | [x] |
| 3   | [x] |
| 4   | [x] |
| 5   | [x] |
| 6   | [x] |
| 7   | [x] |
| 8   | [x] |
| 9   | [x] |

Array of SSL with empty pointers

| 0   | [x]                                         |
| --- | ------------------------------------------- |
| 1   | [x]                                         |
| 2   | [x]                                         |
| 3   | [x]                                         |
| 4   | [x]                                         |
| 5   | \|Annie\| \|5.9\| -> \|Abe\| \|6.5\| -> [x] |
| 6   | [x]                                         |
| 7   | [x]                                         |
| 8   | [x]                                         |
| 9   | [x]                                         |
```C++
std::vector<std::list<std::pair<std::string, double>>> h(10, {});
```

| 0   | [x]                                         |
| --- | ------------------------------------------- |
| 1   | [x]                                         |
| 2   | [x]                                         |
| 3   | [x]                                         |
| 4   | [x]                                         |
| 5   | \|Annie\| \|5.9\| -> \|Abe\| \|6.5\| -> [x] |
| 6   | \|Tom\| \|5.5\| -> [x]                      |
| 7   | [x]                                         |
| 8   | [x]                                         |
| 9   | [x]                                         |
```
(Ace, 6.1)
```

To get a good runtime the goal is to try to keep the chains short because the runtime is the average length of chain.

TO BE CONTINUED

