'''
Interface Segregation Principle (ISP): A client should not be forced to depend on interfaces it does not use. In other words, classes should not implement interfaces that contain methods they do not need.
'''
# Violation of ISP:


from abc import ABC, abstractmethod


class Machine:
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


'''
This class violates the ISP because it includes methods that are not relevant to all the clients that use it. For example, some clients may only need to print documents and do not require the fax or scan methods.
'''

# Following ISP:


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Scanable(ABC):
    @abstractmethod
    def scan(self):
        pass


class Faxable(ABC):
    @abstractmethod
    def fax(self):
        pass


class Printer(Printable):
    def print(self):
        print("Printing...")


class Scanner(Scanable):
    def scan(self):
        print("Scanning...")


class FaxMachine(Faxable):
    def fax(self):
        print("Faxing...")


class AllInOne(Printable, Scanable, Faxable):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

    def fax(self):
        print("Faxing...")


def print_document(printer: Printable):
    printer.print()


def scan_document(scanner: Scanable):
    scanner.scan()


def fax_document(fax_machine: Faxable):
    fax_machine.fax()


def main():
    printer = Printer()
    scanner = Scanner()
    fax_machine = FaxMachine()
    all_in_one = AllInOne()

    print_document(printer)
    scan_document(scanner)
    fax_document(fax_machine)

    # All-in-one device can perform all the operations
    print_document(all_in_one)
    scan_document(all_in_one)
    fax_document(all_in_one)


if __name__ == '__main__':
    main()

'''
Here, we have separated the interface into smaller, more specific interfaces that can be implemented by clients based on their requirements. We have also created a composite interface called AllInOne that combines all three interfaces and can be used by clients that need all three functionalities. By doing so, we have followed the ISP and ensured that the clients are not forced to implement unnecessary methods.
'''
