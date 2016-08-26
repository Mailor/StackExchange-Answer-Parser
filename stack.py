import stackexchange

class __SEAPI(str):
    def __call__(self):
        return stackexchange.Site(self)
try:
	forum = str(raw_input("Enter the stackexchange forum url (e.g. puzzling.stackexchange.com): "))
	forum_wrapper = __SEAPI(forum)
	site = stackexchange.Site(forum_wrapper)
	site.be_inclusive()

	id = int(raw_input("Enter the question ID: "))
	question = site.question(id)

	for answer in question.answers:
		print
		print('-'*80)
		print
		print(answer.body)
except:
	print("Oops! Something went wrong! Did you type the inputs in correctly?")