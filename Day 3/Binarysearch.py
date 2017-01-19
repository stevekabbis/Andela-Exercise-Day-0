class BinarySearch(list):
	def __init__(self,comp1,comp2):
	  data = []
	  data.append(comp2)
	  list_len = 1
	  while list_len < comp1:
	    data.append(data[list_len -1] + comp2)
	    list_len +=  1
	  super(BinarySearch,self).__init__(data)
	  self.length = len(data)

	def search(self,number):
		count  = 0
		start  = 0
		self.length = len(self)
		final  = self.length - 1
		mid_point = int((final) / 2)
		pt_location = {'count':'','index':''}
		while start < mid_point:
			
			if (start == mid_point) and (self[start] > number):
				index = -1 
				pt_location["count"] = self.length
				pt_location["index"] = index
				return pt_location
			
			elif self[start] == number:
				index = start
				pt_location["count"] = count
				pt_location["index"] = index
				return pt_location
			elif self[last] == number:
				index = final
				pt_location["count"] = count
				pt_location["index"] = index
				return pt_location
			elif self[mid_point] == number:
				index = mid_point
				pt_location["count"] = count
				pt_location["index"] = index
				return pt_location
			else:
				if self[mid_point] > number:
					final = mid_point - 1
					start = start + 1
					mid_point = (final + start)//2
				else:
					start = mid_point + 1
					final = final - 1
					mid_point = ((final + start)//2) + 1
			count += 1
		pt_location = {'count':count,'index':-1}		
		return pt_location
