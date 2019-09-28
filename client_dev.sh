mkdir -p ./app/static
rm -R ./app/static/*
cd ./client
PUBLIC_URL=http://127.0.0.1:5000/ npm run build
mv ./build/** ../app/static
