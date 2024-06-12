/***
 * Task 12. In stock?
 * Requirements:
 *
 * Make sure to use promisify with Redis
 * Make sure to use the await/async keyword to get the value from Redis
 * Make sure the format returned by the web application is always JSON and not text
 */
import express from 'express';
import { promisify } from 'util';
import redis from 'redis';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250',
    price: 50, initialAvailableQuantity: 4,
  },
  { itemId: 2, itemName: 'Suitcase 450',
    price: 100, initialAvailableQuantity: 10,
  },
  { itemId: 3, itemName: 'Suitcase 650',
    price: 350, initialAvailableQuantity: 2,
  },
  { itemId: 4, itemName: 'Suitcase 1050',
    price: 550, initialAvailableQuantity: 5,
  },
];

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

function getItemById(id) {
  return listProducts.filter((i) => i.itemId === id)[0];
}

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}
const port = 1245;
const st = { status: 'Product not found' };
const app = express();
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const i = getItemById(itemId);

  if (!i) {
    res.json(st);
    return;
  }
  const reservedStock = await getCurrentReservedStockById(itemId);
  const stock =
    reservedStock !== null ? reservedStock : i.initialAvailableQuantity;
  i.currentQuantity = stock;
  res.json(i);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const noStock = { status: 'Not enough stock available', itemId };
  const confirmed = { status: 'Reservation confirmed', itemId };
  const i = getItemById(itemId);
  if (!i) {
    res.json(st);
    return;
  }
  let reservedStock = await getCurrentReservedStockById(itemId);
  if (reservedStock === null) reservedStock = i.initialAvailableQuantity;

  if (reservedStock <= 0) {
    res.json(noStock);
    return;
  }
  reserveStockById(itemId, Number(reservedStock) - 1);
  res.json(confirmed);
});
