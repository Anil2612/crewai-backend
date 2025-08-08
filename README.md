source venv/bin/activate 
uvicorn main:app --reload

lsof -ti :8000
kill -9 PID