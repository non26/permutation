## Permutation
If we have a set of number,[0,1,2,3]  and we need to arrange it all 4 element when the order matters, we will
have ([0,1,2,3].length)!, which is 4! in the example, but what if we need to select a set of [0,1,2,3], "r" elements,
the number of permutation of r elements when r<=[0,1,2,3].length is  ([0,1,2,3].length)!/([0,1,2,3].length-r)!

## Idea behind this
    1. find the parant of selection
    2. swap the parant fo each position 
example:<br>
1.if we have a set of 4 elements, which is [0,1,2,3], if we select all of them, the number of permutation here will be
4! which is 24 sets, and the parant will be only one set for this case, which is [0,1,2,3] and then swap<br>
[0,1,2,3]<br>
[0,1,3,2]<br>
[0,3,2,1]<br>
[0,3,1,2]<br>
[0,1,3,2]<br>
[0,1,2,3]<br>
we see that [0,1,3,2] can't swap anymore, then we use another set like [0,1,3,2] for continue swapping until it gets 24
sets of permutation [0,1,2,3]

2.if we want to select the 3 element out of [0,1,2,3], so the parent will not only be just one like the above<br>
### find the parent, in case of the first index is 0
[0,1,2] this is the initial, then increase the last index by one<br>
[0,1,3]<br>
[0,1,4] at this point, we will see that the last index is 4 but, we don't 4 in [0,1,2,3], so we need the increase the index
before the index of value 4, which is,<br>
[0,2,1]<br>
[0,2,2] can't repeat the same number<br>
[0,2,3]<br>
[0,2,4] can't be<br>
[0,3,1]<br>
[0,3,2]<br>
[0,3,3] can't be<br>
[0,3,4]<br>
[0,4,5] at this point we can't continue with [0,4,5] <br>

>so the overal parents will be<br>
> [0,1,2]<br>
> [0,1,3]<br>
> [0,2,1]<br>
> [0,2,3]<br>
> [0,3,1]<br>
> [0,3,2]<br>

and then swap like the fisrt example.

                                        


## Do Next
1. add more test
2. edit mark down