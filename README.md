## WASTE MANAGEMENT - SCIENCE FAIR

### Follow these steps just after cloning:
#### Create a virtual environment
```python -m venv virtual```

#### Activate the environment
```virtual/scripts/activate``` (For windows)<br>
```source virtual/bin/activate``` (For Mac/Linux)

#### Install all packages
```pip install -r requirements.txt```

#### Run AI Image Classifier
```streamlit run waste.py --server.port 8501```

#### Run server & Enjoy
```python server.py```

1131dec8678b051757b347881f1d29d05ee07901

### For Database Connection
```flask db init```<br>
```flask db migrate -m "Message"```<br>
```flask db upgrade```<br>
