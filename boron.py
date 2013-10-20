#!/usr/bin/env python


"""

Help text goes here

"""

import sys
import getopt

import re

class Parade:

	class Node:
					def __init__(self,name):
									self.predArr = []
									self.name = name
									self.color = 0 # Color 0 => node is white (unvisited)
									               # Color 1 => node is grey (visited once)
																 # Color 2 => node is black (sorted)

					def __addpred__(self,name):
									self.name = name

					def __pred__(self,name):
									self.name = name

	def __init__(self): 
		self.graph = {}
		self.ordering = []

	def printGraph(self):
		for key in self.graph.keys():
			print "%s must come after:" % (key)
			for node in self.graph[key].predArr:
				print node.name

			print

	def sort(self):
		for key in self.graph.keys():
			if  self.graph[key].color == 0:
				self.__visit__(self.graph[key])

	def __visit__(self, node):
		# This node is already sorted
		if node.color == 2:
			return

		# This node is already visited, and 
		# an ancestor node has lead us back 
		# to it, so we must have a loop
		if node.color == 1:
			print "Graph is not a DAG"
			sys.exit(1)

		node.color = 1

		# Visit predecessors
		for predecessor in node.predArr:
			self.__visit__(predecessor)

		# Now all predecessors must be
		# in the ordering, so this node
		# can be be added.
		node.color = 2
		#self.ordering.insert(0,node)
		self.ordering.append(node)
		
	def output(self):
		for node in self.ordering:
			print node.name

	def input(self,fname):
		fin = open(fname)

		for line in fin:
			# strip newline from the input.
			line = line.rstrip()
			# Now split apart the line.  
			m = re.match("(.*) comes (before|after) (.*)", line)

			# default direction of arrow in graph
			head = m.group(1)
			tail = m.group(3)

			# Now check to see if the direction above is okay.  For this 
			# algorithm we have an edge from x to y if x comes after y in 
			# parade.  Thus, we swap if x comes before y

			if m.group(2) == "before":
				swap = head
				head = tail
				tail = swap

			if not self.graph.__contains__(head):
				newNode = self.Node(head)
				self.graph[head] = newNode

			if not self.graph.__contains__(tail):
				newNode = self.Node(tail)
				self.graph[tail] = newNode

			self.graph[head].predArr.append(self.graph[tail])

class Usage(Exception):
        def __init__(self, msg):
                self.msg = msg

def main(argv=None):
	if argv is None:
 		argv = sys.argv

	parade = Parade()
	parade.input(argv[1])
	parade.printGraph()
	parade.sort()
	parade.output()

        # parse command line arguments
        #try:
       #         try:
                        # Parse options and args.  If = comes after an option name, that option must get a value.  
                        # Otherwsie it must be used alone.   This function enforces that.
                        #opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "accessId", "secretKey=", "hosts="])
                #except getopt.error, msg:  
                #        raise Usage(msg)

                # If we need a config file, read it here
                #print opts
                #print args
                #if len(opts) == 0:
                #        try: 
                #                print args[0]
                #        except:
                #                raise Usage("Please provide either command line options or a config file")
                #else:
                #        # process options on commandline, by looping across an array of tuples (o,a) where 
                        # o is an option name, and v is the value of the option 
                #        for o,v in opts:
                #                if o in ("-h", "--help"):
                #                        print __doc__  # Prevent above help string
                #                        return 0

                #                if o == "--accessId":
                #                        accId = a
                #                elif  o == "--secretKey":
                #                        secKey = a
                #                else:
                #                        hostArr = a.split(',')


                # Now we have options, so make sure that we got good ones, or bail.
                #if accId.__len__() == 0 or secKey.__len__() == 0 or hostArr.__len__() == 0 or hostArr[0].__len__ == 0:
                #        raise Usage("one or more system parameters missing")

                #poll(accId, secKey, hostArr)


        #except Usage, err:
        #        print >>sys.stderr, err.msg
        #        print >>sys.stderr, "for help use --help"
        #        return 2



if __name__ == "__main__":
        sys.exit(main())
