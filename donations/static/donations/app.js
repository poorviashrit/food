document.addEventListener('DOMContentLoaded', () => {
 const deadline=document.getElementById('best_before');
 if(deadline){const d=new Date();d.setMinutes(d.getMinutes()-d.getTimezoneOffset());deadline.min=d.toISOString().slice(0,16);}
 document.querySelectorAll('.delete-form').forEach(form=>form.addEventListener('submit',e=>{if(!confirm('Delete this food donation listing?'))e.preventDefault();}));
});
