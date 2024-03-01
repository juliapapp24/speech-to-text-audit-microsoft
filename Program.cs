using System;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using Microsoft.CognitiveServices.Speech;
using Microsoft.CognitiveServices.Speech.Audio;

class Program
{
  static async Task Main(string[] args)
  {
    if (args.Length > 0)
    {
      string name = args[0];
      await RunSpeechToText(name);
    }
    else
    {
      Console.WriteLine("Please provide a name as a command-line argument.");
    }
  }

  static async Task RunSpeechToText(string name)
  {
    string azureKey = "c6330815003e4d7d94e03f17aa36a880";
    string azureLocation = "eastus";
    string textFile = $"output_files/{name}_output.txt";
    string waveFile = $"audio_files/{name}_audio.wav";

    try
    {
      FileInfo fileInfo = new FileInfo(waveFile);
      if (fileInfo.Exists)
      {
        var speechConfig = SpeechConfig.FromSubscription(azureKey, azureLocation);
        using var audioConfig = AudioConfig.FromWavFileInput(fileInfo.FullName);
        using var speechRecognizer = new SpeechRecognizer(speechConfig, audioConfig);
        var stopRecognition = new TaskCompletionSource<int>();

        FileStream fileStream = File.OpenWrite(textFile);
        StreamWriter streamWriter = new StreamWriter(fileStream, Encoding.UTF8);

        speechRecognizer.Recognized += (s, e) =>
        {
          switch (e.Result.Reason)
          {
            case ResultReason.RecognizedSpeech:
              streamWriter.WriteLine(e.Result.Text);
              break;
            case ResultReason.NoMatch:
              Console.WriteLine("Speech could not be recognized for " + name + ".");
              break;
          }
        };

        speechRecognizer.Canceled += (s, e) =>
        {
          if (e.Reason != CancellationReason.EndOfStream)
          {
            Console.WriteLine("Speech recognition canceled for " + name + ".");
          }
          stopRecognition.TrySetResult(0);
          streamWriter.Close();
        };

        speechRecognizer.SessionStopped += (s, e) =>
        {
          Console.WriteLine("Speech recognition stopped for " + name + ".");
          stopRecognition.TrySetResult(0);
          streamWriter.Close();
        };

        Console.WriteLine("Speech recognition started for " + name + ".");
        await speechRecognizer.StartContinuousRecognitionAsync();
        Task.WaitAny(new[] { stopRecognition.Task });
        await speechRecognizer.StopContinuousRecognitionAsync();
      }
      else
      {
        Console.WriteLine($"Audio file {waveFile} not found.");
      }
    }
    catch (Exception ex)
    {
      Console.WriteLine(ex.Message);
    }
  }
}
