# import Queue
# import threading
# import urllib2 as ul

# # called by each thread
# def get_url(q, url):
# 	q.put(ul.urlopen(url).read())

# theurls = ["https://www.google.com.sg/?gfe_rd=cr&ei=54GhVuizL6Gl8weftLPACQ", "http://mainichi.jp/"]

# q = Queue.Queue()

# for u in theurls:
# 	t = threading.Thread(target=get_url, args=(q,u))
# 	t.daemon = True
# 	t.start()

# s = q.get()
# print s



############## old version of multithreading

# import thread
# import time

# # define a function for thread
# def print_time(threadname, delay):
# 	count = 0
# 	while count < 5:
# 		time.sleep(delay)
# 		count +=1
# 		print "%s: %s" % (threadname, time.ctime(time.time()))

# # create 2 threads as follows
# try:
# 	thread.start_new_thread(print_time, ("Thread-1", 2, ))
# 	thread.start_new_thread(print_time, ("Thread-2", 4, ))
# except:
# 	print "Error: Unable to start thread"

# while 1:
# 	pass


############# new version of multithreading

# import threading as th
# import time as t

# exitFlag = 0

# class myThread(th.Thread):

# 	def __init__(self, threadID, name, counter):
# 		th.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter

# 	def run(self):
# 		print "Starting " + self.name
# 		print_time(self.name, self.counter, 5)
# 		print "Exiting " + self.name

# def print_time(threadname, delay, counter):
# 	while counter:
# 		if exitFlag:
# 			threadname.exit()
# 		t.sleep(delay)
# 		print "%s: %s" % (threadname, t.ctime(t.time()))
# 		counter -= 1

# # create new thread
# thread1 = myThread("one", "Thread-1", 1)
# thread2 = myThread("two", "Thread-2", 2)

# # start new threads
# thread1.start()
# # thread2.run()
# print "\n"
# print "Exiting Main Thread"
# print "I have plenty of time to spend"
# print "yay"

# thread2.start()


############ synchonizing thread
# import threading
# import time

# class myThread(threading.Thread):

# 	def __init__(self, threadID, name, counter):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter
# 	def run(self):
# 		print "Starting " + self.name
# 		# get Lock to synchronize threads
# 		threadLock.acquire()
# 		print_time(self.name, self.counter, 3)
# 		# free Lock to release next thread
# 		threadLock.release()

# def print_time(threadname, delay, counter):
# 	while counter:
# 		time.sleep(delay)
# 		print "%s: %s" % (threadname, time.ctime(time.time()))
# 		counter -= 1

# threadLock = threading.Lock()
# threads = []

# # create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 1)

# # start new threads
# thread1.start()
# thread2.start()

# # add threads to thread list
# threads.append(thread1)
# threads.append(thread2)

# # wait for all threads to complete
# for t in threads:
# 	t.join()
# print "Exiting Main Thread"



########## Multithreaded priority queue

import Queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):

	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q

	def run(self):
		print "Starting " + self.name
		process_data(self.name, self.q)
		print "Exiting " + self.name

def process_data(threadname, q):
	while not exitFlag:
		queueLock.acquire()
		if not workqueue.empty():
			data = q.get()
			queueLock.release()
			# time.sleep(2)
			print "%s processing %s" % (threadname, data)
		else:
			queueLock.release()
		time.sleep(1)

threadlist = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", "Thread-6"]
nameList = ["One", "Two", "Three", "Four", "Five", "Six"]
queueLock = threading.Lock()
workqueue =  Queue.Queue(10)
threads = []
threadID = 1

# create new thread
for tn in threadlist:
	thread = myThread(threadID, tn, workqueue)
	thread.start()
	threads.append(thread)
	threadID += 1

# fill the queue
queueLock.acquire()
for word in nameList:
	workqueue.put(word)
queueLock.release()

#wait for queue to empty
while not workqueue.empty():
	pass

# notify threads it's time to exit
exitFlag = 1

print "Exiting Main Thread"
