SELECT "Liste des potions : Numéro, libellé, formule et constituant principal" as "Question 1";
SELECT * FROM potion;

SELECT "Liste des noms des trophées rapportant 3 points" as "Question 2";
SELECT NomCateg FROM categorie WHERE NbPoints = 3;

SELECT "Liste des villages (noms) contenant plus de 35 huttes" as "Question 3";
SELECT NomVillage FROM village WHERE NbHuttes > 35;

SELECT "Liste des trophées (numéros) pris en mai / juin 52" as "Question 4";
SELECT NumTrophee FROM trophee WHERE DatePrise between "2052/05/01" and "2052/06/30";

SELECT "Noms des habitants commençant par 'a' et contenant la lettre 'r'" as "Question 5";
SELECT Nom FROM habitant WHERE Nom LIKE "a%" and Nom LIKE '%r%';

SELECT "Numéros des habitants ayant bu les potions numéros 1, 3 ou 4" as "Question 6";
SELECT NumHab FROM absorber WHERE NumPotion IN (1, 2, 4) GROUP BY NumHab ORDER BY NumHab;

SELECT "Liste des trophées : numéro, date de prise, nom de la catégorie et nom du preneur" as "Question 7";
SELECT NumTrophee, DatePrise, c.NomCateg, h.Nom FROM trophee t
JOIN categorie c ON c.CodeCat = t.CodeCat
JOIN habitant h ON t.NumPreneur = h.NumHab;

SELECT "Nom des habitants qui habitent à Aquilona" as "Question 8";
SELECT h.Nom FROM habitant h
JOIN village v ON v.NomVillage = "Aquilona" AND v.NumVillage = h.NumVillage;

SELECT "Nom des habitants ayant pris des trophées de catégorie Bouclier de Légat" as "Question 9";
SELECT h.nom FROM trophee t
JOIN habitant h ON t.NumPreneur = h.NumHab
JOIN categorie c ON c.CodeCat = t.CodeCat AND c.NomCateg = "Bouclier de Légat";

SELECT "Liste des potions fabriquées par Panoramix : libellé, formule et constituant principal." as "Question 10";
SELECT LibPotion, Formule, ConstituantPrincipal FROM potion p
JOIN fabriquer f ON p.NumPotion = f.NumPotion
JOIN habitant h ON h.NumHab = f.NumHab AND h.Nom = 'Panoramix';

(SELECT numbhab FROM habitant WHERE nom = 'Panoramix');

SELECT "Liste des potions absorbées par Homéopatix" as "Question 11";
SELECT DISTINCT (LibPotion) FROM absorber a
JOIN potion p ON p.NumPotion = a.NumPotion
JOIN habitant h ON h.NumHab = a.NumHab AND h.Nom = 'Homéopatix';

SELECT "Liste des habitants (noms) ayant absorbé une potion fabriquée par l'habitant numéro 3" as "Question 12";
SELECT DISTINCT (h.Nom) FROM habitant h
JOIN absorber a ON h.NumHab = a.NumHab
JOIN potion p ON a.NumPotion = p.NumPotion
JOIN fabriquer f ON a.NumPotion = f.NumPotion
WHERE f.NumHab = 3;

SELECT "Liste des habitants (noms) ayant absorbé une potion fabriquée par Amnésix" as "Question 13";
SELECT DISTINCT (h.Nom) FROM habitant h
JOIN absorber a ON h.NumHab = a.NumHab
JOIN potion p ON a.NumPotion = p.NumPotion
JOIN fabriquer f ON a.NumPotion = f.NumPotion
WHERE f.NumHab = (SELECT numHab FROM habitant WHERE nom = 'Amnésix');

SELECT "Nom des habitants dont la qualité n'est pas renseignée" as "Question 14";
SELECT nom FROM habitant WHERE numqualite IS NULL;

--JOIN qualite q ON q.numqualite = h.numqualite
--WHERE h.numqualite =]

SELECT "Nom des habitants ayant consommé la potion magique n°1 (c'est le libellé de la potion) en février 52" as "Question 15";
SELECT h.nom FROM habitant h
JOIN absorber a ON a.numhab = h.numhab
JOIN potion p ON p.numpotion = a.numpotion
WHERE p.LibPotion = 'Potion magique n°1' AND a.DateA BETWEEN '2052-02-01' AND '2052-02-29';

--a.dateA = between "2052/02/01 00:00:00" and "2052/02/28 00:00:00" AND
SELECT "Nom et âge des habitants par ordre alphabétique" as "Question 16";
SELECT nom, age FROM habitant
ORDER BY nom;

SELECT "Liste des resserres classées de la plus grande à la plus petite : nom de resserre et nom du village" as "Question 17";
SELECT r.NomResserre, v.nomvillage FROM resserre r
JOIN village v ON v.numvillage = r.numvillage
ORDER BY r.Superficie DESC;

SELECT "Nombre d'habitants du village numéro 5" as "Question 18";
SELECT numHab FROM habitant WHERE numvillage = 5;

Nombre de points gagnés par Goudurix.

SELECT "Nombre de points gagnés par Goudurix" as "Question 19";
SELECT SUM(c.nbpoints) FROM categorie c
JOIN trophee t ON c.codecat = t.codecat
JOIN habitant h ON h.numhab = t.numpreneur
WHERE h.NumHab = (SELECT numHab FROM habitant WHERE nom = 'Goudurix');

SELECT "Date de première prise de trophée" as "Question 20";
SELECT MIN(DatePrise) from trophee;


SELECT "Nombre de louches de potion magique n°2 (c'est le libellé de la potion) absorbées" as "Question 21";
SELECT SUM(a.quantite) FROM absorber a
JOIN potion p ON p.numpotion = a.numpotion AND p.libpotion = 'Potion magique n°2';


SELECT "Superficie la plus grande" as "Question 22";
SELECT MAX(Superficie) FROM resserre;

SELECT "Nombre d'habitants par village (nom du village, nombre)" as "Question 23";
SELECT DISTINCT COUNT(h.numhab), v.nomvillage FROM habitant h
JOIN village v ON v.numvillage = h.numvillage
GROUP BY v.nomvillage;

SELECT "Nombre de trophées par habitant" as "Question 24";
SELECT DISTINCT COUNT(t.numtrophee), h.nom FROM habitant h
JOIN trophee t ON t.numpreneur = h.numhab
GROUP BY h.nom;

SELECT "Moyenne d'âge des habitants par province (nom de province, calcul)" as "Question 25";
SELECT AVG(h.age), p.nomprovince FROM habitant h
JOIN village v ON v.numvillage = h.numvillage
JOIN province p ON v.numprovince = p.numprovince
GROUP BY p.nomprovince;

SELECT "Nombre de potions différentes absorbées par chaque habitant (nom et nombre)" as "Question 26";
SELECT p.numpotion, h.numhab, h.nom FROM habitant h
JOIN absorber a ON a.numhab = h.numhab
JOIN potion p ON p.numpotion = a.numpotion
GROUP BY h.numhab;


--hutte trier dans l'ordre et prendre que le premier'


