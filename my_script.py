# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
# For Commit sake , just for fun
from pystrich.datamatrix import DataMatrixEncoder

encoder = DataMatrixEncoder('This is a DataMatrix.')
encoder.save('./datamatrix_test.png')
print(encoder.get_ascii())
