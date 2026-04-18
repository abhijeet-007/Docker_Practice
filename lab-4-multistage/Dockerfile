# Stage 1: Build
FROM node:20-alpine AS build
WORKDIR /app
COPY package.json .
RUN npm install -production

# Stage 2: Run
FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/node_modules ./node_modules
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
