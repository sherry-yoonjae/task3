FROM slave4.wizeye.com.cn:5000/ubuntu-python
COPY dict_search.py /home/dict_search.py
CMD python /home/dict_search.py