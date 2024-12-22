import os
import markdown
from datetime import datetime
import glob

def generate_blog_html():
    # Template for the blog page
    blog_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name - Blog</title>
    <!-- Include your CSS here -->
</head>
<body>
    <nav>
        <ul>
            <li><a href="index.html">About</a></li>
            <li><a href="resume.html">Resume</a></li>
            <li><a href="blog.html">Blog</a></li>
        </ul>
    </nav>

    <div class="container">
        <h1>Blog Posts</h1>
        {blog_posts}
    </div>
</body>
</html>
'''

    # Get all markdown files from the posts directory
    posts = []
    for md_file in glob.glob('posts/*.md'):
        with open(md_file, 'r') as f:
            content = f.read()
            # Convert markdown to HTML
            html_content = markdown.markdown(content)
            
            # Get file creation date for the post date
            creation_date = datetime.fromtimestamp(os.path.getctime(md_file))
            date_str = creation_date.strftime('%B %d, %Y')
            
            # Create blog post HTML
            post_html = f'''
            <article class="blog-post">
                <h2>{os.path.basename(md_file).replace('.md', '')}</h2>
                <div class="blog-meta">
                    Posted on {date_str}
                </div>
                <div class="blog-content">
                    {html_content}
                </div>
            </article>
            '''
            posts.append((creation_date, post_html))
    
    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x[0], reverse=True)
    
    # Generate the full blog page
    blog_content = blog_template.format(blog_posts=''.join([p[1] for p in posts]))
    
    # Write to blog.html
    with open('blog.html', 'w') as f:
        f.write(blog_content)

if __name__ == '__main__':
    generate_blog_html()

