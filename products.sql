--Series of SQL statements to reset the products db
INSERT INTO "public"."products" (name, price, category, image, tax, description)
VALUES ('Holly/Phoenix Feather Wand', 50.00, 'wands', 'https://cdn.shopify.com/s/files/1/0221/1146/products/Harry_Potter_Ollivanders_Wand_Scaled_large.png?v=1546860074', 0.06, 'Eleven inch wand made of Holly with a phoenix feather core'),
       ('Vine/Dragon Heartstring Wand', 50.00, 'wands', 'https://cdn.shopify.com/s/files/1/0221/1146/products/Hermione_Granger_Ollivanders_Wand_Scaled_large.png?v=1546860165', 0.06, 'Ten and three quarters inch wand made of Vine with a dragon heartstring core'),
       ('Elder/Thestral Tail Hair Wand', 100.00, 'wands', 'https://cdn.shopify.com/s/files/1/0221/1146/products/Albus_Dumbledore_Ollivanders_Wand_Scaled_large.png?v=1546859532', 0.06, 'Elder Wand. Enough Said.'),
       ('Time Turner', 30000.00, 'dangerous', 'https://cdn.thisiswhyimbroke.com/images/hermoines-time-turner-necklace.jpg', 0.06, 'Powerful magical object that allows the user to turn back time. Dangerous if you are seen.'),
       ('Sword of Gryffindor', 100000.00, 'dangerous', 'https://i.pinimg.com/originals/2f/7e/03/2f7e0388841e36271513caf64a5e5dc4.png', 0.06, 'Historical magical object. Presents itself to any worthy Gryffindor.'),
       ('Firebolt', 15000.00, 'quidditch', 'https://i.pinimg.com/originals/6f/2e/14/6f2e143ef7cdf2a058a0bc115f565b0b.jpg', 0.06, 'International standard broom. Currently fastest model in the world.'),
       ('Gryffindor Quidditch Robes', 120.00, 'quidditch', 'https://shop.universalorlando.com/merchimages/p-gryffindor-quidditch-robe-replica-rep-qddtch-cape.jpg', 0.06, 'High quality, aerodynamic, comfortable quidditch robes.'),
       ('Unicorn Hair', 20.00, 'potion ingredients', 'https://static.wikia.nocookie.net/pottermore/images/a/ad/PM_UnicornTailHair_Object.jpg/revision/latest/scale-to-width-down/596?cb=20181205032914', 0.06, 'Very strong and useful in a number of potions.'),
       ('Bezoar', 15.00, 'potion ingredients', 'https://resize.hswstatic.com/w_796/gif/bezoar-stone.jpg', 0.06, 'Found in the stomach of a goat it is an antidote for most poisons.')


--Command to update column in db
UPDATE "public"."products"
SET column = value,
WHERE condition