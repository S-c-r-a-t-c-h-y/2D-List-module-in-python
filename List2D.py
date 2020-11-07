class List2D :
	

    def __init__(self, cols=0, rows=0, value=''):
        """ initialize itself """
        self.value = []
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            self.value.append([])
            for j in range(cols):
                self.value[i].append('')
        self.fill(value)

             
    def show(self):
        """ print itself """
        for i in range(self.rows) :
            print(str(self.value[i]) + "\n", end='')
    
    
    def change(self, x, y, value):
        """ replace the value of the object at the coordinate (x,y) by the given value """
        if x > self.cols -1 or y > self.rows -1:
        	raise IndexError('Change index out of range')

        self.value[y][x] = value 
    
    
    def fill(self,value):
        """ fill all the empty spaces with the given value """
        self.normalize()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.value[i][j] == '' :
                    self.value[i][j] = value
    
    
    def get(self, x, y):
        """ return the value of the object of coordinates (x,y) """
        if self.cols == 0 and self.rows == 0:
        	raise IndexError('Get from an empty list')
        if x > self.cols -1 or y > self.rows -1:
        	raise IndexError('Get index out of range')

        return self.value[y][x]


    def pop(self, x, y):
        """ Remove and return item at index (default last).
	
	    Raises IndexError if list is empty or index is out of range """

        if self.cols == 0 and self.rows == 0:
        	raise IndexError('Pop from an empty list')
        if x > self.cols -1 or y > self.rows -1:
        	raise IndexError('Pop index out of range')

        result = self.value[y][x]
        self.change(x,y,'')
        return result
  

    def normalize(self, *args):
        """ Fill all the rows or just the selected one so that they fit the cols size """
        
        if args:
            while len(self.value[args[0]]) < self.cols :
                self.value[args[0]-1].append('')
        else :
            for i in range(self.rows):
                while len(self.value[i]) < self.cols:
                    self.value[i].append('')
    

    def add_rows(self, times=1, index=9223372036854775807, value=''):
        """ Add a single row at the end or at the given index"""

        self.rows += times
        for i in range(times) :
            self.value.insert(index, [])
        self.fill(value)


    def add_cols(self, nb=1, index=9223372036854775807, value=''):
        """ Add a specified colon at the specified index (default to the end) """

        self.cols += nb
        for i in range(self.rows):
        	for j in range(nb):
        		self.value[i].insert(index, value)


    def clear(self) :
    	""" Empty the list """
    	self.value.clear()
    	self.rows = 0
    	self.cols = 0


    def count(self, value) :
    	""" Return number of occurrences of value """
    	result = 0
    	for row in self.value:
    		result += row.count(value)
    	return result


    def copy(self) :
    	""" Return a shallow copy of the list """
    	result = List2D(self.cols, self.rows)
    	result.value = self.value
    	return result


    def index(self, value, from_end=False) :
    	""" Return index of value.

    	Raises ValueError if the value is not present. """

    	result = None
    	if from_end :
    		for i in range(self.rows):
    			if self.value[i].count(value) != 0:
    				result = (self.value[i].index(value), i)
    	else:
    		for i in range(self.rows-1, 0, -1):
    			if self.value[i].count(value) != 0:
    				result = (self.value[i].index(value), i)

    	if result == None:
    		raise ValueError(f"'{value}' is not in list")
    	return result


    def all_indices(self, value, from_end=False) :
    	""" Return index of value.

    	Raises ValueError if the value is not present. """

    	result = []
    	if from_end :
    		for i in range(self.rows):
    			if self.value[i].count(value) != 0:
    				result.append((self.value[i].index(value), i))
    	else:
    		for i in range(self.rows-1, 0, -1):
    			if self.value[i].count(value) != 0:
    				result.append((self.value[i].index(value), i))

    	if result == []:
    		raise ValueError(f"'{value}' is not in list")
    	return result


    def remove(self, value) :
    	""" Remove the first occurence of the value """

    	for i in range(self.rows):
    		if self.value[i].count(value) != 0:
    			self.change(self.value[i].index(value), i, '')

    def reverse(self, rows=True, cols=True) :
    	""" Reverse the colons, the rows, or both by default """
    	if rows:
    		for row in self.value:
    			row.reverse()
    	if cols:
    		for i in range(self.cols):
    			rev = []
    			for row in self.value:
    				rev.append(row[i])
    			rev.reverse()
    			for j in range(self.rows):
    				self.value[j][i] = rev[j]

    def sort(self, rows=True, cols=True, key=None, reverse=False):
    	""" Sort the colons, the rows, or both by default """
    	if rows:
    		for row in self.value:
    			row.sort(key=key, reverse=reverse)
    	if cols:
    		for i in range(self.cols):
    			l = []
    			for row in self.value:
    				l.append(row[i])
    			l.sort(key=key, reverse=reverse)
    			for j in range(self.rows):
    				self.value[j][i] = l[j]
    	