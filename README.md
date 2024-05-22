# speech-to-text-audit-microsoft

## Creating an Azure AI services account using the Azure portal
The multi-service resource is listed under Azure AI services > Azure AI services multi-service account in the portal. To create a multi-service resource follow these instructions:

- Create an Azure portal if you don't already have one. You can use your Cornell email to create an account. If you already have an account, then sign in at the same link.

- Create a multi-service resource here

- This should take you to a page titled "Create Azure AI services". Provide the information it asks for.

- After you are done, with the previous step, you should see a green checkmark and a confirmation saying "Your deployment is complete". If you see this, now click on "Deployment details"

- Now, click on the link under "Resource" that should be named whatever you named it in step 3.

- You should now see a subpage called "Essentials" in the middle of the screen. Click on the the link at "Manage keys". This should take you to a page called "Keys and Endpoint"

- Once you are at the page "Keys and Endpoint" copy "KEY 1".

- Now open Program.cs. Locate line 25: string azureKey = "c6330815003e4d7d94e03f17aa36a880". replace the value of it with the value you copied from "KEY 1"

- Now go back to the page "Keys and Endpoint" and copy the value at "Location/Region".

- Now open Program.cs. Locate line 25: string azureLocation = "eastus";. Replace the value of it with the value you copied from "Location/Region"

- Save your changes!

- Now go back to here. Go to unit 3 out of 8 by clicking the arrow.

- Follow the directions in Unit 3 in the terminal of THE JUPYTER NOTEBOOK

- After finishing Unit 3, you should be all set to continue to the next step, which is installing dependencies. If you run into any troubles, just continue onto unit 4 and follow links wherever needed.

## Dependencies [DO THIS BEFORE RUNNING ANY CODE]
o be able to run the algorithm you will need to install serval dependencies and set up a virtual environent. Follow these steps to ensure smooth running of the algorithm:

Open your terminal in VS code by going to Terminal >> New Terminal and type dotnet add package Microsoft.CognitiveServices.Speech

Now, still in the terminal, type code Program.cs to ensure that the system is set up correctly.

To be able to run C# code from a Jupyter Python kernel, ensure that you have .NET installed To download do the following steps:

Go to https://dotnet.microsoft.com/en-us/download
Download the appropriate package for your operating system
To find the path of where .NET was installed open your terminal and do the following:
type "dotnet" into your terminal to ensure that it downloaded correctly it should output something like this:

(base) yourname@dhcp-vl2041-25861 ~ % dotnet

Usage: dotnet [options]

Usage: dotnet [path-to-application]

Options:

 -h|--help         Display help.

 --info            Display .NET information.

 --list-sdks       Display the installed SDKs.

 --list-runtimes   Display the installed runtimes.

path-to-application:

The path to an application .dll file to execute.

If it's successful, type "where dotnet" into your terminal That should output something like this:

(base) yourname@dhcp-vl2041-25861 ~ % where dotnet

 /usr/local/share/dotnet/dotnet

Copy the line "/usr/local/share/dotnet/dotnet". This may be slightly different for you and that okay. In the code cell below (3 cells below) replace the line dotnet_path = "/usr/local/share/dotnet/dotnet" with your actual path
