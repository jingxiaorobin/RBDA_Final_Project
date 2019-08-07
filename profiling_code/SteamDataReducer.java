
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.*;
import java.util.*;
import java.lang.*;
import java.util.regex.*;
public class SteamDataReducer
extends Reducer<Text, Text, Text, Text> {
@Override
  public void reduce(Text key, Iterable<Text> values, Context context)
  throws IOException, InterruptedException {
    double overallRating= 0.0;
    for (Text value : values) {
      String temp = value.toString();
      String result = temp.replaceAll("\"", "");
      overallRating = Double.parseDouble(result.replaceAll("%", ""))/100.00;

    }
    context.write(key, new Text(Double.toString(overallRating)));

  }
}
