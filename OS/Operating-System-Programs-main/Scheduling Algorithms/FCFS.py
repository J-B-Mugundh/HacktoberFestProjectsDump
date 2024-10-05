class Process:
	def __init__(self,num,at,bt):
		self.process_no = num
		self.AT = at
		self.BT = bt
		self.exit = 0
		
	def tat(self,exit):
		self.exit = exit
		self.TAiT = self.exit - self.AT
		return self.TAT
		
	def wt(self):
		self.WT = self.TAT - self.BT
		return self.WT
		
if __name__ == "__main__":
	
	process = []
	for i in range(5):
		at = int(input("Enter arrival time: "))
		bt = int(input("Enter burst time: "))
		
		process.append(Process(i,at,bt))		
	process = sorted(process,key = lambda process:process.AT)
	exit_time = 0
	awt = 0
	flag = False
	for pro in range(len(process)):
		temp_exit = exit_time
		exit_time = max(exit_time,process[pro].AT) + process[pro].BT
		if not flag:   
			print(f'| {temp_exit}',end=" ")
			flag = True
		if process[pro].AT > temp_exit:
			print(f"{process[pro].AT}",end=" ")
		print(f"P{process[pro].process_no}",end=" ")   

		print(f"{exit_time}",end=" | ")
		
		
		tat = process[pro].tat(exit_time)
		wt = process[pro].wt()
		awt += wt
	print("\n")
	awt = awt / len(process)
	
	print("Process","\t","Arrival Time","\t","Burst Time","\t","Turn Around Time","\t","Wait Time")
	for i in range(len(process)):
		print(process[i].process_no,"\t\t\t",process[i].AT,"\t\t",process[i].BT,"\t\t",process[i].TAT,"\t\t",process[i].WT)
	print("Average Waiting Time: ",awt)
	print("Throughput: ",exit_time / len(process))




