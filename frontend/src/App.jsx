import { useState } from 'react';
import { Search, Activity, CheckCircle, AlertTriangle, Lightbulb, Loader2 } from 'lucide-react';

const INVESTIGATION_STEPS = [
  "Understanding business question...",
  "Identifying relevant metrics...",
  "Generating hypotheses...",
  "Querying analytical tools...",
  "Testing alternative explanations...",
  "Ranking root causes...",
  "Synthesizing recommendations..."
];

function App() {
  const [question, setQuestion] = useState("Why is delivery time so high in Semi-Urban areas compared to Metropolitan?");
  const [isLoading, setIsLoading] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  const handleInvestigate = async () => {
    if (!question.trim()) return;
    
    setIsLoading(true);
    setResult(null);
    setError("");
    setCurrentStep(0);

    // Simulate the investigation steps visually for the user
    const stepInterval = setInterval(() => {
      setCurrentStep((prev) => (prev < INVESTIGATION_STEPS.length - 1 ? prev + 1 : prev));
    }, 800);

    try {
      const response = await fetch('http://127.0.0.1:8000/investigate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
      });

      if (!response.ok) throw new Error("Investigation failed. Check if the backend is running.");
      
      const data = await response.json();
      clearInterval(stepInterval);
      setCurrentStep(INVESTIGATION_STEPS.length - 1);
      setResult(data);
    } catch (err) {
      clearInterval(stepInterval);
      setError(err.message || "An unknown error occurred");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen p-8 max-w-5xl mx-auto font-sans">
      {/* Header */}
      <header className="mb-8 text-center">
        <h1 className="text-3xl font-bold text-slate-800 flex items-center justify-center gap-3">
          <Activity className="w-8 h-8 text-blue-600" />
          Autonomous Analytics Investigator
        </h1>
        <p className="text-slate-500 mt-2">
          Traditional BI tells you WHAT happened. This system investigates WHY and WHAT to do next.
        </p>
      </header>

      {/* Input Section */}
      <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 mb-8">
        <label className="block text-sm font-semibold text-slate-700 mb-2">Ask a business question:</label>
        <div className="flex gap-3">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleInvestigate()}
            className="flex-1 px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
            placeholder="e.g., Why did average delivery time increase last month?"
          />
          <button
            onClick={handleInvestigate}
            disabled={isLoading}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white px-6 py-3 rounded-lg font-semibold flex items-center gap-2 transition"
          >
            {isLoading ? <Loader2 className="w-5 h-5 animate-spin" /> : <Search className="w-5 h-5" />}
            Investigate
          </button>
        </div>
      </div>

      {/* Loading / Progress State */}
      {isLoading && (
        <div className="bg-blue-50 border border-blue-200 rounded-xl p-6 mb-8">
          <h3 className="font-semibold text-blue-800 mb-4 flex items-center gap-2">
            <Loader2 className="w-5 h-5 animate-spin" />
            AI Investigation in Progress
          </h3>
          <div className="space-y-3">
            {INVESTIGATION_STEPS.map((step, index) => (
              <div key={index} className={`flex items-center gap-3 transition-opacity duration-300 ${index <= currentStep ? 'opacity-100' : 'opacity-30'}`}>
                {index < currentStep ? (
                  <CheckCircle className="w-5 h-5 text-green-600" />
                ) : index === currentStep ? (
                  <Loader2 className="w-5 h-5 text-blue-600 animate-spin" />
                ) : (
                  <div className="w-5 h-5 rounded-full border-2 border-slate-300" />
                )}
                <span className={`text-sm ${index <= currentStep ? 'text-slate-800 font-medium' : 'text-slate-500'}`}>
                  {step}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Error State */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 p-4 rounded-xl mb-8 flex items-center gap-3">
          <AlertTriangle className="w-5 h-5" />
          {error}
        </div>
      )}

      {/* Results Section */}
      {result && !isLoading && (
        <div className="space-y-6 animate-fade-in">
          
          {/* Executive Summary */}
          <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <h2 className="text-xl font-bold text-slate-800 mb-3 flex items-center gap-2">
              <Activity className="w-5 h-5 text-blue-600" />
              Executive Summary
            </h2>
            <p className="text-slate-700 leading-relaxed">{result.executive_summary}</p>
          </div>

          <div className="grid md:grid-cols-2 gap-6">
            {/* Root Causes */}
            <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
              <h2 className="text-xl font-bold text-slate-800 mb-4 flex items-center gap-2">
                <AlertTriangle className="w-5 h-5 text-amber-600" />
                Most Likely Contributors
              </h2>
              <ul className="space-y-3">
                {result.root_causes.map((cause, i) => (
                  <li key={i} className="flex gap-3 text-slate-700">
                    <span className="font-bold text-amber-600">{i + 1}.</span>
                    {cause}
                  </li>
                ))}
              </ul>
            </div>

            {/* Recommendations */}
            <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
              <h2 className="text-xl font-bold text-slate-800 mb-4 flex items-center gap-2">
                <Lightbulb className="w-5 h-5 text-green-600" />
                Recommended Actions
              </h2>
              <ul className="space-y-3">
                {result.recommendations.map((rec, i) => (
                  <li key={i} className="flex gap-3 text-slate-700">
                    <span className="font-bold text-green-600">•</span>
                    {rec}
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Evidence Ledger */}
          <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <h2 className="text-xl font-bold text-slate-800 mb-4">Evidence Ledger</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-sm text-left">
                <thead className="text-xs text-slate-500 uppercase bg-slate-50 border-b">
                  <tr>
                    <th className="px-4 py-3">Hypothesis</th>
                    <th className="px-4 py-3">Metric</th>
                    <th className="px-4 py-3">Finding</th>
                    <th className="px-4 py-3 text-right">Value</th>
                    <th className="px-4 py-3 text-right">Sample</th>
                    <th className="px-4 py-3 text-center">Confidence</th>
                  </tr>
                </thead>
                <tbody>
                  {result.evidence.map((ev, i) => (
                    <tr key={i} className="border-b hover:bg-slate-50">
                      <td className="px-4 py-3 font-medium text-slate-800">{ev.hypothesis_id}</td>
                      <td className="px-4 py-3 text-slate-600">{ev.metric}</td>
                      <td className="px-4 py-3 text-slate-700">{ev.finding}</td>
                      <td className="px-4 py-3 text-right font-mono text-slate-800">{ev.quantitative_value}</td>
                      <td className="px-4 py-3 text-right font-mono text-slate-600">{ev.sample_size}</td>
                      <td className="px-4 py-3 text-center">
                        <span className={`px-2 py-1 rounded-full text-xs font-semibold ${
                          ev.confidence === 'High' ? 'bg-green-100 text-green-800' :
                          ev.confidence === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
                          'bg-red-100 text-red-800'
                        }`}>
                          {ev.confidence}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* Limitations */}
          <div className="bg-slate-100 p-6 rounded-xl border border-slate-200">
            <h2 className="text-sm font-bold text-slate-600 uppercase tracking-wider mb-2">Data Limitations</h2>
            <p className="text-slate-700 text-sm">{result.limitations}</p>
          </div>

        </div>
      )}
    </div>
  );
}

export default App;