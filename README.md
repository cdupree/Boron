This is a solution to a puzzle I found online.  Since it is used
by a company as a way to solicit interest from programmers I'm not
putting the website I found it on.  In any case, if you happen to
have found this answer, and the original site consider that you
aren't doing yourself a favor by submitting this code, or someone
elses.  That will just catch up to you at some point.

The goal of the problem is take input of the form

A comes before B
B comes after C
....

and produce an ordering which honors the input, such
as

A 
C
B

To do this I use an algorithm called topological sort.   I start
by reading in the list of ordering preferences, and form a graph
of nodes.  This graph is directed meaning that whenever A must occur
after B, then an arrow is drawn between these two nodes in the
graph.  In the code this is done by having each node keep an array
of its predecessor nodes, although there are other ways to keep
this information.

One the input is read we start processing the nodes.   Originally
each node is colored "white" which means we haven't processed it.
As "white" nodes are discovered in th graph we visit the node
coloring it "gray" to indicate that it has been seen in the processing.
Then we immediately visit the predecessors of that node.   This
method of traversing a graph is known as a depth first search,
because we go as deep as possible into the graph as we can before
we act on a node.   The alternatie is breadth first search
which would act on a node, then on its predecessor's, and so 
on marching out into the graph layer by layer.  If at some
point we visit a node which has been colored gray, then we
know that we have visited that node before which means that there
is a cycle in this graph.   Such as cycle prevents there from
being a topological sort.   Once all of a node's predecessors
are processed, they are in the sort.  This means that we
can color the node "white", and safely place it into the
sort.
