# Fun Python Tidbits

## Optimizing Python

Python has some tried-and-true functions that can allow for speed up. (Though, if you *really* want a speedup, perhaps don't use Python?)

### Iterating over an array

Instead of 

```
i = 0
while i < len(arr):
  print(arr[i])
```

Try

```
for i in arr:
  print(i)
```

(Good practice would also suggest you name the variable.)

If you need the index, try:

```
for idx, ele in arr:
  print(i, ele)
```

The reason why the latter two are both faster is because it creates an iterable which is a pointer. 

A similar idea goes for traversing backwards:

```
for ele in reverse(arr):
  print(ele)
```

This I haven't been using before! I used to always do `for ele in arr[::-1]`, but that creates a shallow copy of the array which can take up time and space! Instead, `reverse` creates an iterable which can be used to more efficiently traverse the array.
