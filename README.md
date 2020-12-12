<h1><span><strong>WELCOME TO AKEYZERR'S PLAYGROUND!</strong></span></h1>

<p>The project consists of two apps - a Blog/Forum-type app, and a ToDo-type app.<br />
In order to access the site, one must register a free account(with a dummy e-mail, but with CAPTCHA).<br />
Registered accounts can upload their own custom profile picture, and update their info and settings.<br />
Additionally, logger-in user can read the full content of any public(*) blog post, can add comments under
the post. When creating own blog post, the user can mark it as &quot;not public&quot;. 
Non-public posts are visible only to their authors in the &quot;All my posts&quot; section. 
In the detail view of a post, the author can edit and delete the post.</p>

<p>Users can create their own tasks in the ToDo app, tag them as &quot;completed&quot; and assign tags to each Task.</p>

<p>&nbsp;</p>

<p>Run these in the DB manager after &#39;migrate&#39; in order to run the project locally:</p>

<p><code>INSERT INTO public.homepage_entry (id, title, implementation, requirement, status, date_created, date_updated, 
created_by_id, state) VALUES (1, &#39;Login/Register&#39;, &#39;Implemented in the &#39;&#39;user&#39;&#39; app. 
user&#39;&#39;s Views handle the registration part and profile update.&#39;, &#39;The project must have login/register 
functionality&#39;, &#39;Completed.&#39;, &#39;2020-11-28 16:34:10.427700&#39;, &#39;2020-11-28 17:18:04.003211&#39;, 1,
 &#39;Mandatory&#39;); INSERT INTO public.homepage_quotes (id, clean_state, quote) VALUES (1, true, &#39;2b || !2b&#39;)
; </code></p>
