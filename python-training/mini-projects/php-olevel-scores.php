<?php
$flash_message = 'Olevel Results';
require_once('db_config.php');
require_once('model.php');
?>

<?php
  // GET ALL THE CANDIDATES JAMB REG NUMBERS FROM JAMB RESULT TABLE
  $olevel = "SELECT regnumber FROM nau_utme";
  $olevel = $connect_db->query($olevel);
  if ($olevel->num_rows > 0) {
    // output data of each row 
?>

<table class="table table-bordered table-responsive">
  <thead>
    <tr>
      <th> RegNo. </th>
      <th> Full Name </th>
      <th> UTME Score </th>
      <th> Olevel Points </th>
      <th> Course </th>
      <th> UTMEsubjects </th>
      <th> OlevelSubjects </th>
      <th> ResultCount </th>
    </tr>
  </thead>
  <tbody>
    <?php
      while($olevel_row = $olevel->fetch_assoc()) { 
        $regno = $olevel_row["regnumber"];

        # GET Candidates O'level Result
        $utmesubjects = "SELECT regnumber,subject,grade,examyear,examtype,examnumber,gradescore FROM nau_exams_sup WHERE regnumber = '$regno'";
        $utmesub = $connect_db->query($utmesubjects);
        if (!empty($utmesub) && $utmesub->num_rows > 0) {
          // code...
          $utmesubArray = array();
          while($utmesub_row = $utmesub->fetch_assoc()) {
             //array_push($utmesubArray, $utmesub_row['subject'].'|'.$utmesub_row['gradescore']);
             array_push($utmesubArray, $utmesub_row['subject'].'|'.$utmesub_row['gradescore']);
           }
        }
        //$utmesub_row['gradescore']
        @$olevel_detail = json_encode($utmesubArray);
        //$olevel_detail = trim($olevel_detail, '[]');
        //$olevel_detail = str_replace("[","",$olevel_detail);
        //$olevel_detail = str_replace("]","",$olevel_detail);
        $olevel_detail = str_replace('"'," ",$olevel_detail);

        $get_main_result = "SELECT
            nau_utme.fullname,
            nau_utme.regnumber,
            nau_utme.subject1 AS s1,
            nau_utme.subject2 AS s2,
            nau_utme.subject3 AS s3,
            nau_utme.engscore AS engscore,
            nau_utme.utme_score AS utmescore,
            SUM(nau_exams_sup.gradescore) AS points,
            nau_utme.course AS course,
            nau_exams_sup.resultcount AS resultcount
            FROM nau_exams_sup
            INNER JOIN nau_utme
            ON
            nau_utme.regnumber = nau_exams_sup.regnumber
            WHERE nau_utme.regnumber = '$regno' 
            AND nau_exams_sup.subject IN (nau_utme.subject1, nau_utme.subject2, nau_utme.subject3, 'ENG') 
            ORDER BY nau_utme.utme_score";

            # SELECT THOSE OLEVEL SUBJECTS
            $matched_olevel = "
              SELECT
                nau_exams_sup.subject as subject,
                nau_olevl_figures.gradescore as gradescore
              FROM nau_exams_sup
              INNER JOIN nau_utme
              ON
              nau_utme.regnumber = nau_exams_sup.regnumber
              WHERE nau_utme.regnumber = '$regno' AND subject 
              IN (nau_utme.subject1, nau_utme.subject2, nau_utme.subject3, 'ENG')";

            $four_olevel = mysqli_query($connect_db, $matched_olevel);

            // while($four_row = mysqli_fetch_array($four_olevel)){
            //   $olevelscore = $matched_olevel_row['subject'];
            //   $olevelgrade = $matched_olevel_row['gradescore'];
            // }

            $main_result = $connect_db->query($get_main_result);

            while($main_result_row = $main_result->fetch_assoc()) { ?>
              <tr>
                <td> <?php echo $olevel_row["regnumber"];?> </td>
                <td> <?php echo $main_result_row["fullname"];?> </td>
                <td> <?php echo $main_result_row["utmescore"];?> </td>
                <td> <?php echo $main_result_row["points"];?> </td>
                <td> <?php echo $main_result_row["course"];?> </td>
                <td> <?php echo $main_result_row["s1"]."|".$main_result_row["s2"]."|".$main_result_row["s3"];?> </td>
                <td> <?php echo $olevel_detail;?> </td>
                <td> <?php echo $main_result_row["resultcount"];?> </td>
              </tr>
      <?php }
    ?>
  <?php }  
  }else {
      $flash_message = "No Data";
  } ?>
  </tbody>
</table>
