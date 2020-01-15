class Computer:
	def __init__(self, srnum):
		self.serial = srnum
		self.memory = None  # GB
		self.hdd = None  # TB
		self.gpu = None

	def __str__(self):
		info = (f'Memory: {self.memory}GB',
				f'Hard Disk: {self.hdd}GB',
				f'Graphics Card: {self.gpu}')
		return '\n'.join(info)


class ComputerBuilder:
	def __init__(self):
		self.computer = Computer('A12345BC657')

	def configure_memory(self, amount):
		self.computer.memory = amount

	def configure_hdd(self, amount):
		self.computer.hdd = amount

	def configure_graphics(self, amount):
		self.computer.gpu = amount


class HardwareEngineer:
	def __init__(self):
		self.builder = None

	def construct_computer(self, memory, hdd, gpu):
		self.builder = ComputerBuilder()
		steps = (self.builder.configure_memory(memory),
				self.builder.configure_hdd(hdd),
				self.builder.configure_graphics(gpu))
		[step for step in steps]

	@property
	def computer(self):
		return self.builder.computer


def main():
	engineer = HardwareEngineer()
	engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
	computer = engineer.computer
	print(computer)

if __name__ == '__main__':
 	main() 
	
