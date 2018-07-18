$(document).ready(function(){


            $('#sample1').fadeTo(0,0); //show
            $('#sample2').fadeTo(0,0);
            $('#sample3').fadeTo(0,0);
            $('#sample4').fadeTo(0,0);
            $('#sample5').fadeTo(0,0);

            $("#image1").click(function(){

                $('#sample1').fadeTo(500,1);
                $('#sample2').fadeTo(500,0);
                $('#sample3').fadeTo(500,0);
                $('#sample4').fadeTo(500,0);
                $('#sample5').fadeTo(500,0);


            });
            $("#image2").click(function(){
                $('#sample2').fadeTo(500,1);
                $('#sample1').fadeTo(500,0);
                $('#sample5').fadeTo(500,0);
                $('#sample3').fadeTo(500,0);
                $('#sample4').fadeTo(500,0);

            });
            $("#image3").click(function(){

                $('#sample3').fadeTo(500,1);
                $('#sample1').fadeTo(500,0);
                $('#sample5').fadeTo(500,0);
                $('#sample2').fadeTo(500,0);
                $('#sample4').fadeTo(500,0);
            });
            $("#image4").click(function(){
                $('#sample4').fadeTo(500,1);
                $('#sample1').fadeTo(500,0);
                $('#sample5').fadeTo(500,0);
                $('#sample2').fadeTo(500,0);
                $('#sample3').fadeTo(500,0);
            });
            $("#image5").click(function(){
                $('#sample5').fadeTo(500,1);
                $('#sample1').fadeTo(500,0);
                $('#sample3').fadeTo(500,0);
                $('#sample2').fadeTo(500,0);
                $('#sample4').fadeTo(500,0);
            });

        });