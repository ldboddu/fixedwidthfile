FROM python:3.9-slim
WORKDIR /app
COPY fixedwidthfile.py .
CMD ["python", "fixedwidthfile.py"]
### instructions to run docker File###
# docker build -t fixedwidthtocsv
# docker run --rm -v $(pwd):/app fixedwidthtocsv
# docker images
# docker tag fixedwidthtocsv ldboddu/fixedwidthcsv:v1.0
# docker push ldboddu/fixedwidthcsv:v1.0
# docker pull ldboddu/fixedwidthcsv:v1.0
