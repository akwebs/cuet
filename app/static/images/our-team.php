<!DOCTYPE html>
<?php include_once("constant.php");
extract($_POST); ?>

<!--[if IE 8 ]><html class="ie ie8" class="no-js" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!--><html class="no-js" lang="en"> <!--<![endif]-->
<head>
<?php 

// Program to display URL of current page. 
  

require_once("inc/head_file_include.php") ; ?>


<link rel="stylesheet" href="css/style1.css"/>
<style>
    @media only screen and (max-width: 980px){
        .hero-image{
            height:25%!important
        }
    }
   .hero-image{
      border-bottom:8px solid #2f3d57; 
background-image: -webkit-linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('<?php echo url;?>images/our-team/OurTeam-ZIPZAP.jpg');
background-image: -o-linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('<?php echo url;?>images/our-team/OurTeam-ZIPZAP.jpg');
background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('<?php echo url;?>images/our-team/OurTeam-ZIPZAP.jpg');
        background-position: center center;
       background-size:cover;
        background-origin: border-box;
        background-repeat: repeat-x;
       height:60%
      
    }
    
    
    .hero-image1{
      border-bottom:8px solid #2f3d57; 
  background-image: linear-gradient(rgba(0, 0, 0, 1), rgba(0, 0, 0, 0.7)), url('<?php echo url;?>images/about-ias/bg-attach1.png');
        background-position: center;
       background-size:cover;
        background-origin: border-box;
        background-repeat: repeat-x;
        background-attachment: fixed;
      
    }
    
    
     
    
    

               
            .line-after-text::after{
                
                content: "   ";
                  
                background-color:#2E3D57;
                height:2px;
                width:100%;
                padding-right: 15px;
                padding-left:15px;
                position:absolute;
                top:50%;
                
                transform: translate(0%, -50%);
               
               
            }

       
    </style>

</head>




<style>
    /* FontAwesome for working BootSnippet :> */


#team {
    background: #eee !important;
}



section {
    padding: 60px 0;
}

/*
section .section-title {
    text-align: center;
    color: #007b5e;
    margin-bottom: 50px;
    text-transform: uppercase;
}
*/

#team .card {
    border: none;
    background: #ffffff;
}

.image-flip:hover .backside,
.image-flip.hover .backside {
    -webkit-transform: rotateY(0deg);
    -moz-transform: rotateY(0deg);
    -o-transform: rotateY(0deg);
    -ms-transform: rotateY(0deg);
    transform: rotateY(0deg);
    border-radius: .25rem;
}

.image-flip:hover .frontside,
.image-flip.hover .frontside {
    -webkit-transform: rotateY(180deg);
    -moz-transform: rotateY(180deg);
    -o-transform: rotateY(180deg);
    transform: rotateY(180deg);
}

.mainflip {
    -webkit-transition: 1s;
    -webkit-transform-style: preserve-3d;
    -ms-transition: 1s;
    -moz-transition: 1s;
    -moz-transform: perspective(1000px);
    -moz-transform-style: preserve-3d;
    -ms-transform-style: preserve-3d;
    transition: 1s;
    transform-style: preserve-3d;
    position: relative;
}

.frontside {
    position: relative;
    -webkit-transform: rotateY(0deg);
    -ms-transform: rotateY(0deg);
    z-index: 2;
    margin-bottom: 30px;
}

.backside {
    
    position: absolute;
    top: 0;
    left: 0;
        
    background: white;
    -webkit-transform: rotateY(-180deg);
    -moz-transform: rotateY(-180deg);
    -o-transform: rotateY(-180deg);
    -ms-transform: rotateY(-180deg);
    transform: rotateY(-180deg);
    -webkit-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
    -moz-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
    box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
}

    
.frontside,
.backside {
   
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    -ms-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-transition: 1s;
    -webkit-transform-style: preserve-3d;
    -moz-transition: 1s;
    -moz-transform-style: preserve-3d;
    -o-transition: 1s;
    -o-transform-style: preserve-3d;
    -ms-transition: 1s;
    -ms-transform-style: preserve-3d;
    transition: 1s;
    transform-style: preserve-3d;
}

.frontside .card,
.backside .card {
    min-height: 300px;
    max-height: 320px;
    overflow: hidden;
    
}

.backside .card a {
    font-size: 18px;
    color: #007b5e !important;
}

.frontside .card .card-title,
.backside .card .card-title {
    color: #007b5e !important;
}

.frontside .card .card-body img {
    width: 70px;
    height: 70px;
    border-radius: 50%;
}
    
    
    .line-after-text{
        
        padding-left:20px;
    }
    .line-after-text::before{
        content:"";
        position:absolute;
        top:10%;
        left:0px;
        
        height:70%;
        width:8px;
        background-color:#2f3d57;
        
        
    }
    </style>
    
    
     <?php require_once("inc/menubar.php"); ?> 
    
<div class="hero-image">  
</div>



         
              
<section id="team" class="pb-5" style="background-color:lightgray!important;">
           <div style=" border-left:45px solid #78aad4; border-right:45px solid #78aad4"></div>

           <div class="container">
           
            
             <div style="position:relative; overflow:hidden; "> <h2 style="" class="section-title h2 text-blue1 text-left line-after-text">  Mentors Panel &nbsp; </h2> </div>
        
                        
           
           
        
        <div class="row pt-1 pb-5">
            <!-- Team member -->
               <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/Pritam%20K%20Goswami.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 ">  CA Pritam K Goswami </span></h3>
                                     <p class="card-text pt-0 mt-0"> International Training Fellow   </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/Pritam%20K%20Goswami.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                 

                                  
                                    </p>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
             <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/abhishek%20sir.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Abhishek Rathi </span></h3>
                                    <p class="card-text pt-0 mt-0">  IIT Delhi Alumnus </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/abhishek%20sir.png" alt="card image">  </p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                <!--    BACK SIDE CONTENT -->

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p> </p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 ">  </span></h3>
                                    <p class="card-text pt-0 mt-0">   </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p>   </p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                <!--    BACK SIDE CONTENT -->

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
             <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p> </p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 ">  </span></h3>
                                    <p class="card-text pt-0 mt-0">   </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p>   </p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                <!--    BACK SIDE CONTENT -->

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
          
         
            

        </div>
        
        
        <!---------------------------- Eminent Panel ------------------------------------->
        

       
       <div style="position:relative; overflow:hidden"> <h2 class="section-title h2 text-blue1 text-left line-after-text">  Eminent Faculties &nbsp; </h2> </div>
        
        
<!--        <h1 class="section-title h1 text-blue1"> Eminent Panel </h1>        -->
        
          <div class="form-row pt-1 pb-2">
            <!-- Team member -->
            <div class="col-md-3 ">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/Dr.%20RUCHIKA%20BATHALA.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Dr. Ruchika Bathala </span></h3>
                                    <p class="card-text pt-0 mt-0"> GS - History Art  & Culture </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/Dr.%20RUCHIKA%20BATHALA.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:80%;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                  
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
                <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/parhlad%20varshney.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Prof. Prahlad Varshney </span></h3>
                                    <p class="card-text pt-0 mt-0"> GS - Geography </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/parhlad%20varshney.png" alt="card image"> </p>  </div>
                                    
                                  <p style="font-size:80%; line-height:80%;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                 
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
         
         
          <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/M.TOFIK%20sir.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Prof. M. Tofik </span></h3>
                                    <p class="card-text pt-0 mt-0">  GS - Economics  </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/M.TOFIK%20sir.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                               

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
            
            
          <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/Dr%20Sapna.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Dr. Sapna Agarwal</span></h3>
                                    <p class="card-text pt-0 mt-0"> Personality Development Trainer  </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/Dr%20Sapna.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                 

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
            
            
               </div>
               
            <div class="form-row pt-1 pb-2">    
            
             <div class="col-md-3 ">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/PieushAgrawal.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Col. Pieush Agrawal </span></h3>
                                      <p class="card-text pt-0 mt-0"> GS - Science & Technology </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/PieushAgrawal.png" alt="card image"> </p>  </div>
                                    
                                  <p style="font-size:80%; line-height:80%;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                  
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            
            
                 <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/Debbie%20%20Coutts.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 ">  Mrs. Debbie  Coutts </span></h3>
                                    <p class="card-text pt-0 mt-0"> English  </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/Debbie%20%20Coutts.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:80%;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
<!--
                                  <ul class="text-left">
                                  
                                  <li style="list-style-type:disc; font-size:85%; line-height:140%;">  M.A. ( History) - Gold Medalist </li>
                                  <li style="list-style-type:disc; font-size:85%; line-height:140%;">  B.Ed </li>
                                  <li style="list-style-type:disc;font-size:85%; line-height:140%;">  PG Diploma in Gandhian Non Violent Conflict Resolution. </li>
                                  <li style="list-style-type:disc;font-size:85%; line-height:140%;">  Ph.D - Research Fellow ( Indian Council of Historical Research, New Delhi) </li>
                                  <li style="list-style-type:disc;font-size:85%; line-height:140%;">  Post Doctoral Research ( Indian Council of Historical Research, New Delhi) </li>
                                  
                                      <li style="list-style-type:disc;font-size:85%; line-height:140%;"> Publication Grant for doctoral thesis from I.C.H.R
Book Published titled " Gandhian theory  and practice of Labour Movement " </li>
                                      <li style="list-style-type:disc;font-size:85%; line-height:140%;">  Presently serving as Chairperson of Geo Genius India.( I.B.G.B Learning Society)</li>
                                  
                                  
                                  
                                  </ul> 
-->
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/Vikas%20sen.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Er. Vikas Sen </span></h3>
                                    <p class="card-text pt-0 mt-0"> General Aptitude & Mental Ability </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/Vikas%20sen.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:80%;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
               
               
               
            <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/Pritam%20K%20Goswami.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 ">  CA Pritam K Goswami </span></h3>
                                     <p class="card-text pt-0 mt-0"> GS - Polity   </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/Pritam%20K%20Goswami.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                             
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
         
         
            

        </div>
        
        
        <!--------------------------------------Executive commette -------------------------------------------->
        
          <div style="position:relative; overflow:hidden"> <h2 class="section-title h2 text-blue1 text-left line-after-text">  Executive Committee &nbsp; </h2> </div>
        
        
                        
           
           
        
        <div class="row pt-1 pb-5">
            <!-- Team member -->
            
            
               <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/lalit-pawar-sir.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 ">  Lalit Panwar </span></h3>
                                     <p class="card-text pt-0 mt-0"> Joint Director <br> Public Relation & Social Responsibility   </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/lalit-pawar-sir.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                              

                                  
                                    </p>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>          
         
               <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/bhawna%20mam.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Bhavna M Trivedi</span></h3>
                                    <p class="card-text pt-0 mt-0"> Joint Director <br> Administration   </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/bhawna%20mam.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
             <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/Dr%20Sapna1.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Dr. Sapna Agarwal</span></h3>
                                    <p class="card-text pt-0 mt-0"> Joint Director <br> Schools  </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/Dr%20Sapna1.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                              
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div> 
            
               <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/sanidhya-sir.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Sanidhya Sharma </span></h3>
                                    <p class="card-text pt-0 mt-0"> Executive <br> Coordination  </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/sanidhya-sir.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                              

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
         
             

             
       
        </div>
        
        
        
        <!-------------------------------------- Founding Members -------------------------------------------->
        <div style="position:relative; overflow:hidden"> <h2 class="section-title h2 text-blue1 text-left line-after-text"> Founding members &nbsp; </h2> </div>
               
        <div class="row pt-1 pb-5">
            <!-- Team member -->
            
            
                       
         
               <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/kapil%20sir.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 ">Kapil Gupta</span></h3>
                                    <p class="card-text pt-0 mt-0"> Co-Founder <br> IAS Foundation Academy  </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/kapil%20sir.png" alt="card image">  </p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                               

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
           
         
              <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    <p><img style="width:160px; height:160px"  class=" img-fluid" src="images/our-team/shital-mam.png" alt="card image"></p>
                                    <h3 class="card-title px-0 my-0"> <span class="text-blue1 "> Shikha Gupta</span></h3>
                                    <p class="card-text pt-0 mt-0"> Co-Founder <br> IAS Foundation Academy  </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px"> <p><img class=" img-fluid" src="images/our-team/shital-mam.png" alt="card image"></p>  </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                            
                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div> 

                    <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    
                                    <p class="card-text pt-0 mt-0">    </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px">   </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                           

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
            
                   <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    
                                    <p class="card-text pt-0 mt-0">    </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px">   </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                           

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
       
        </div>
        
     <!-------------------------------------- Our Associates -------------------------------------------->
        <div style="position:relative; overflow:hidden"> <h2 class="section-title h2 text-blue1 text-left line-after-text"> Our Associates &nbsp; </h2> </div>
               
        <div class="row pt-1 pb-5">
            <!-- Team member -->
            
            
                       
         
               <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    
                                    <p class="card-text pt-0 mt-0">    </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px">   </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                           

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
            
       <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    
                                    <p class="card-text pt-0 mt-0">    </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px">   </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                           

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
            
                   <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    
                                    <p class="card-text pt-0 mt-0">    </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px">   </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                           

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
            
                   <div class="col-md-3">
                <div class="image-flip" >
                    <div class="mainflip flip-0">
                        <div class="frontside">
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                    
                                    <p class="card-text pt-0 mt-0">    </p>
                                   
                                </div>
                            </div>
                        </div>
                       
                            <div class="backside" id="backside" style="z-index:30!important">
                            
                            <div style="position:relative; z-index:30;" class="pb-3">
                            
                            
                            <div class="card py-auto my-auto">
                                <div class="card-body text-center">
                                   <div style="padding-left:80px; padding-right:80px">   </div>
                                    
                                  <p style="font-size:80%; line-height:110%; z-index:99999;" class="card-text pt-n1 mt-n2 text-left"> 
                                  
                           

                                  
                                   <br>
  
                                   
                                </div>
                            </div>
                        
                        </div>
                        
                        
                        
                        </div>
                    </div>
                </div>
            </div>
            
             
       
        </div>    
        
        
        
        
        
        
        
        
    </div>
        
    </section>
              
              
         
           
           
           
	
 
		
		
 
		<!--end info service-->
    
         
       
<!---------------------course detail-------------------------->
    
  
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Counter-Up/1.0.0/jquery.counterup.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/waypoints/4.0.1/jquery.waypoints.js"></script>
        
    <?php include_once("inc/footer.php"); ?>
	<?php include_once("inc/copyright.php"); ?>
	<?php include_once("inc/js_file.php"); ?>
        
        
        
       
   
</body>
</html>
