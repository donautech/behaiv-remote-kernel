mkdir -p ./app/static
rm -R ./app/static/*
cd ./client
PUBLIC_URL=http://127.0.0.1:5000/web/ npm run build
mv ./build/** ../app/static
