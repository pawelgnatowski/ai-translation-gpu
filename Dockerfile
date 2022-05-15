FROM nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04 as base
RUN apt update && apt install -y python3-pip

FROM base
COPY /app /app

WORKDIR /app
RUN pip3 install -r /app/requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

EXPOSE 5000
#  run the app as a web server
CMD ["python3","app.py"]
# run the app as a server and run workload from within container
# CMD [ "bash" ] 

# docker build -t ai-translation-gpu-app .
# for single GPU server you can use:
# docker run -idt --rm --gpus all -v /home/p/vsProjects/pythonPlayground/ai-translation-gpu/app/data:/app/data -p 5030:5000 --name ai-translate-app ai-translation-gpu-app 