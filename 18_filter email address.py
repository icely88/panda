import pandas as pd
emails = pd.Series(['buying books at amazom.com',
                    'rameses@egypt.com',
                    'matt@t.co',
                    'narendra@modi.com'])
import re
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
valid=emails.str.findall(pattern, flags=re.IGNORECASE)
print([x[0]for x in valid if len(x)])
