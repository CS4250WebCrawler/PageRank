import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.*;


public class CPPCrawler {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        //links to crawl
        ArrayList<String> toCrawl = new ArrayList<>();
        //links that have been crawled
        ArrayList<String> linksCrawled = new ArrayList<>();
        //to help see how many pages we crawled so far
        int count = 0;
        //key: page, value: arraylist of pages key points to
        //ex: if A point to B, then A is key and B is added to the arraylist
        Map<String, ArrayList> linked = new HashMap<String, ArrayList>();
        //the seed
        toCrawl.add("https://www.cpp.edu/");
        //while size of links crawled is less than the max number of pages we want (500)
        while (linksCrawled.size()<500){
            String URL = toCrawl.remove(0);
            try {
                //if we haven't crawled it yet
                if (!linksCrawled.contains(URL)) {
                    //connect to the URL
                    Document document = Jsoup.connect(URL).get();
                    //if connects then
                    //we will crawl it so add it to linksCrawled
                    linksCrawled.add(URL);
                    //total number of valid outlinks in URL
                    int outCount = 0;
                    //select all links
                    Elements linksOnPage = document.select("a[href]");
                    //for each link that is an https containing cpp.edu
                    for (Element page : linksOnPage) {
                        if (page.attr("abs:href").startsWith("https")
                                && page.attr("abs:href").contains("cpp.edu")){
                            String extractedLink = page.attr("abs:href");
//                            System.out.println(extractedLink);
                            //add it to crawl if it hasn't been crawled
                            if (!linksCrawled.contains(extractedLink)) {
                                toCrawl.add(extractedLink);
                            }
                            // for each valid link, update the count for total number of outlinks for URL
                            outCount++;
                            //update linked hashmap
                            if (linked.containsKey(URL)){
                                if(!linked.get(URL).contains(extractedLink))
                                    linked.get(URL).add(extractedLink);
                            }
                            else {
                                linked.put(URL, new ArrayList<String>());
                                linked.get(URL).add(extractedLink);
                            }
                        } //end of if page contains a cpp.edu
                    }//end of for ea page in linkOnPage
                    //just for seeing how far into the crawl it is
                    count++;
                    System.out.println(count);
                }//end of if linksCrawled contains URL
            } catch (Exception e) {
//            System.err.println("For '" + URL + "': " + e.getMessage());
            }
            //if we already crawled the URL, go back to top of while and check next toCrawl link
        }//end of while

        // get rid of links that weren't crawled
        for (String key : linked.keySet()){
            //to prevent the concurrent modification exception, use a separate arraylist to store stuff we want to delete
            ArrayList<String> toRemove =  new ArrayList<>();
            for (Object link : linked.get(key)){
                //if a link wasn't crawled, add it to the toRemove list
                if (!linksCrawled.contains(link.toString())){
                    toRemove.add((String)link);
                }
            }
            //done iterating, now we can remove the links
            for (String dud : toRemove){
                linked.get(key).remove(dud);
            }
        }
        PrintWriter matrix = new PrintWriter("CPP_Matrix.txt");
        PrintWriter pages = new PrintWriter("CPP_Pages.txt");
        ArrayList<Float> temp = new ArrayList();
        //row
        for (String x : linksCrawled) {
            //clear the temp arraylist so we can print each new row to txt file
            temp.clear();
            //column
            for (String key : linksCrawled) {
                //if the key doesn't point to any pages at all
                if (!linked.containsKey(key)){
                    temp.add((float)(0));
                } else {
                    //if the key points to x print 1/key's total number of outlinks
                    if (linked.get(key).contains(x)){
                        temp.add((float)1/(float)linked.get(key).size());
                    } else {
                        temp.add((float)(0));
                    }
                }
            }//end of column iteration
//            System.out.println(temp);
            //printing the row to txt file
            int index = 0;
            for (float num : temp){
                //if we haven't reached the end of the row, include the space
                if (index != temp.size()-1){
                    matrix.print(num + " ");
                } else { //we reached the end, no space needed
                    matrix.print(num);
                }
                index++;
            }
            //if x is not the last element in linksCrawled
            if (linksCrawled.indexOf(x) < linksCrawled.size()-1){
                matrix.println();
            } //else don't go to next line because this is the last row of matrix
            pages.println(x);
        }//end of row iteration
        pages.close();
        matrix.close();
    }//end of main
}