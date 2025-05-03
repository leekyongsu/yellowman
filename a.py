3

import streamlit as st



st.write("Hello, *World!* :sunglasses:")
st.write("이경수, *바보!* :sunglasses:")
st.write("건양대, *재난안전소방학과* :angry:")

st.image('강아지.png')
st.image('dog.jpg')
st.image('이미지.jpg')
color = st.radio('color', ('blue', 'red', 'orange', 'green'), horizontal =True)

f'aa :{color}[bb]'
st.sidebar.write('사이드바')

'# *파이썬* 재밌네'
'## 파이썬 *재밌네*'
'### *파이썬 재밌네*'
'#### 파이썬 재밌네'
'##### :red[파이썬 재밌네]'
'###### 파이썬 재밌네'

st.html(' <H1> ✅파이썬의 [세계에] 오신걸 환영합니다.<H1>')
st.html(' <H2> 파이썬의 세계에 오신걸 환영합니다.<H2>')
st.html(' <H3> 파이썬의 세계에 오신걸 환영합니다.<H3>')
st.html(' <H10> 파이썬의 세계에 오신걸 환영합니다.<H10>')

st.write("봄날, *여행가자* :cool:")
import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)



import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(18, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

