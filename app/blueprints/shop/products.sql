--Series of SQL statements to reset the products db
INSERT INTO "public"."products" (name, price, category, image, tax, description)
VALUES ('Holly/Phoenix Feather Wand', 50.00, 'wand', 'https://cdn.shopify.com/s/files/1/0221/1146/products/Harry_Potter_Ollivanders_Wand_Scaled_large.png?v=1546860074', 0.06, 'Eleven inch wand made of Holly with a phoenix feather core'),
       ('Vine/Dragon Heartstring Wand', 50.00, 'wand', 'https://cdn.shopify.com/s/files/1/0221/1146/products/Hermione_Granger_Ollivanders_Wand_Scaled_large.png?v=1546860165', 0.06, 'Ten and three quarters inch wand made of Vine with a dragon heartstring core'),
       ('Elder/Thestral Tail Hair Wand', 100.00, 'wand', 'https://cdn.shopify.com/s/files/1/0221/1146/products/Albus_Dumbledore_Ollivanders_Wand_Scaled_large.png?v=1546859532', 0.06, 'Elder Wand. Enough Said.')
