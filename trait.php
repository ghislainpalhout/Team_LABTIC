<?php
$ligne = 1; // compteur de ligne
$fic = fopen("resultat.csv", "a+");
while($tab=fgetcsv($fic,1024,';'))
{
$champs = count($tab);//nombre de champ dans la ligne en question
echo "<b> Les " . $champs . " champs de la ligne " . $ligne . " sont :</b><br />";
$ligne ++;
//affichage de chaque champ de la ligne en question
for($i=0; $i<$champs; $i ++)
{
echo $tab[$i] . "<br />";
}
}
?> 