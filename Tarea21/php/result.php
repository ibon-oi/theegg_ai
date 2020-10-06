<html>
<body>
<?php $numero = $_POST["num"]; ?>

El número introducido es <?php echo $numero; ?><br>
<?php
$den = 10000;
$num = $numero * 10000;
$i = $num;
$count = 0;
while ($i > 1)
{
    # Si el numerador y el denominador son divisibles entre i, se asignan nuevos denominador y numerador
    if ( $num % $i == 0 && $den % $i == 0 )
    {
        $num = $num / $i;
        $den = $den / $i;
    }
    $i = $i - 1;
    $count = $count + 1;
}
echo "El resultado es ".$num." / ".$den." Iteraciones realizadas: ".$count;
?>


</body>
</html>