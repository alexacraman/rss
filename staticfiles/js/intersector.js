window.addEventListener('DOMContentLoaded', () =>{
    
    
    
    const paragraphs = document.querySelectorAll('.paras');
    const companies = document.querySelectorAll('.cos');
    
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            // console.log(entry.target)
            if (entry.isIntersecting){
                entry.target.classList.add('aniShont');
                entry.target.classList.add('aniShont05');
                // return;
            }
            // else{
            //     entry.target.classList.remove('aniShont');
            //     entry.target.classList.remove('aniShont05');
            // }
            
        })
    })
    
    paragraphs.forEach(paras =>{
        observer.observe(paras);
    })
    companies.forEach(cos =>{
        observer.observe(cos);
    })
    
    
    });