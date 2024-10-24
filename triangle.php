<?php
function triangle($n) {
    $triangle = [];
    for ($i = 0; $i < $n; $i++) {
        if ($i == 0) {
            $triangle[] = [1];
        } else {
            $row = [1];
            for ($j = 1; $j < $i; $j++) {
                $row[] = $triangle[$i - 1][$j - 1] + $triangle[$i - 1][$j];
            }
            $row[] = 1;
            $triangle[] = $row;
        }
    }
    return $triangle;
}
?>
//for mr jb
